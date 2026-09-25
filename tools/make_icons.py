"""图标派生脚本（唯一设计源头）。

以 tools/src/weblogo.jpg（用户提供的站点徽标源图）为源，生成：
favicon.png / favicon.ico / apple-touch-icon.png / assets/img/logo.png / assets/img/og.png。
取源图上部徽章区域派生，所有尺寸由脚本缩放，禁止手工修改生成的图片。
运行：conda run -n main_website --no-capture-output python tools/make_icons.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "tools" / "src" / "weblogo.jpg"

LIGHT_BG = (246, 248, 252)
TEXT = (28, 39, 51)


def load_emblem() -> Image.Image:
    """加载源图并裁出徽章本体（按行墨量剖面定位徽章与下方文字之间的空白带）。"""
    img = Image.open(SRC).convert("RGB")
    w, h = img.size
    gray = ImageOps.grayscale(img)
    mask = gray.point(lambda p: 255 if p < 242 else 0)
    ink = [sum(mask.crop((0, y, w, y + 1)).getdata()) // 255 for y in range(h)]

    # 徽章顶部：第一行有明显墨量
    top = next((y for y in range(h) if ink[y] > w * 0.01), 0)

    # 自顶向下找第一段 >=12 行的近零墨量空白带（徽章与文字之间的间隔）
    gap_start = None
    y = top
    while y < h:
        if ink[y] < w * 0.005:
            run = 0
            yy = y
            while yy < h and ink[yy] < w * 0.005:
                run += 1
                yy += 1
            if run >= 12:
                gap_start = y
                break
            y = yy
        else:
            y += 1
    bottom = (gap_start if gap_start is not None else int(h * 0.72)) - 2

    # 徽章区域内取水平边界，居中裁成正方形（圆形徽章宽高应接近）
    zone_mask = mask.crop((0, top, w, bottom))
    l, _t, r, _b = zone_mask.getbbox() or (0, 0, w, bottom - top)
    wd, ht = r - l, bottom - top
    side = max(wd, ht)
    cx = (l + r) // 2
    x0 = max(0, min(w - side, cx - side // 2))
    y0 = max(0, top - (side - ht) // 2)
    return img.crop((x0, y0, x0 + side, y0 + side))


def rounded_icon(emblem: Image.Image, size: int, radius_ratio: float = 0.22) -> Image.Image:
    """徽章置于白底圆角方形画布中央（RGBA，圆角透明）。"""
    ss = 4  # 超采样抗锯齿
    s = size * ss
    canvas = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle([0, 0, s - 1, s - 1], radius=int(s * radius_ratio), fill=(255, 255, 255, 255))
    inner = int(s * 0.84)
    em = emblem.resize((inner, inner), Image.LANCZOS)
    off = (s - inner) // 2
    canvas.paste(em, (off, off))
    # 重新套圆角 alpha，避免徽章溢出圆角
    alpha = Image.new("L", (s, s), 0)
    ImageDraw.Draw(alpha).rounded_rectangle([0, 0, s - 1, s - 1], radius=int(s * radius_ratio), fill=255)
    canvas.putalpha(alpha)
    return canvas.resize((size, size), Image.LANCZOS)


def main() -> None:
    emblem = load_emblem()

    # favicon.png（64）与 favicon.ico（16/32/48）
    icon64 = rounded_icon(emblem, 64)
    icon64.save(ROOT / "favicon.png")
    icon256 = rounded_icon(emblem, 256)
    icon256.save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

    # apple-touch-icon（180，满方形不透明）
    touch = Image.new("RGB", (180, 180), (255, 255, 255))
    t_emblem = emblem.resize((150, 150), Image.LANCZOS)
    touch.paste(t_emblem, (15, 15))
    touch.save(ROOT / "apple-touch-icon.png")

    # 页头 logo（512）
    rounded_icon(emblem, 512).save(ROOT / "assets" / "img" / "logo.png")

    # og:image（1200x630，纯白底与源图白底无缝融合 + 徽章 + 标题）
    og = Image.new("RGB", (1200, 630), (255, 255, 255))
    em = emblem.resize((300, 300), Image.LANCZOS)
    og.paste(em, ((1200 - 300) // 2, 70))
    d = ImageDraw.Draw(og)
    try:
        font_big = ImageFont.load_default(size=58)
        font_sub = ImageFont.load_default(size=30)
        t1 = "Weibaba Software"
        t2 = "Software Portfolio · 软件作品集"
        b1 = d.textbbox((0, 0), t1, font=font_big)
        b2 = d.textbbox((0, 0), t2, font=font_sub)
        d.text(((1200 - (b1[2] - b1[0])) / 2, 412), t1, fill=TEXT, font=font_big)
        d.text(((1200 - (b2[2] - b2[0])) / 2, 496), t2, fill=(91, 107, 124), font=font_sub)
    except TypeError:
        pass  # Pillow 过旧不支持字号参数时仅保留图形标识
    og.save(ROOT / "assets" / "img" / "og.png")

    print("icons generated from", SRC)


if __name__ == "__main__":
    main()

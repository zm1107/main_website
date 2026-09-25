"""图标派生脚本（唯一设计源头）。

生成 favicon.png / favicon.ico / apple-touch-icon.png / assets/img/logo.png / assets/img/og.png。
所有尺寸均由本脚本的 1024px 主图缩放派生，禁止手工修改生成的图片。
运行：conda run -n main_website --no-capture-output python tools/make_icons.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]

ACCENT = (47, 111, 237)
WHITE = (255, 255, 255)


def rounded_square(size: int, radius_ratio: float = 0.225) -> Image.Image:
    """生成主标识：圆角方形底 + 粗笔画 W。"""
    ss = 4  # 超采样倍数，缩小时抗锯齿
    s = size * ss
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, s - 1, s - 1], radius=int(s * radius_ratio), fill=ACCENT)

    # W 折线（两端高、中间峰略低），圆头圆角连接
    k = s / 1024
    pts = [
        (192 * k, 322 * k),
        (355 * k, 706 * k),
        (512 * k, 468 * k),
        (669 * k, 706 * k),
        (832 * k, 322 * k),
    ]
    d.line(pts, fill=WHITE, width=int(128 * k), joint="curve")
    r = int(64 * k)
    for p in (pts[0], pts[-1]):
        d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=WHITE)
    return img.resize((size, size), Image.LANCZOS)


def save_rgba(img: Image.Image, rel: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)


def main() -> None:
    # favicon.png（64）与 favicon.ico（16/32/48）
    master = rounded_square(1024)
    save_rgba(master.resize((64, 64), Image.LANCZOS), "favicon.png")
    ico_src = master.resize((256, 256), Image.LANCZOS)
    ico_src.save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

    # apple-touch-icon（180，不透明底）
    touch = Image.new("RGB", (180, 180), ACCENT)
    touch.paste(rounded_square(180), (0, 0), rounded_square(180))
    touch.save(ROOT / "apple-touch-icon.png")

    # 站点 logo（512）
    save_rgba(rounded_square(512), "assets/img/logo.png")

    # og:image（1200x630）
    og = Image.new("RGB", (1200, 630), ACCENT)
    mark = rounded_square(300)
    og.paste(mark, (450, 105), mark)
    try:
        font = ImageFont.load_default(size=64)
        d = ImageDraw.Draw(og)
        text = "Weibaba Software"
        bbox = d.textbbox((0, 0), text, font=font)
        w = bbox[2] - bbox[0]
        d.text(((1200 - w) / 2, 470), text, fill=WHITE, font=font)
    except TypeError:
        pass  # Pillow 过旧不支持字号参数时仅保留图形标识
    og.save(ROOT / "assets/img/og.png")

    print("icons generated under", ROOT)


if __name__ == "__main__":
    main()

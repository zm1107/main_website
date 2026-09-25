# Weibaba 软件 · 产品主站

#README #官网 #主站

[English](README.en.md)

<p align="center"><img src="assets/img/weblogo.jpg" alt="Weibaba Zhang SoftWare 徽标" width="160"></p>

**Weibaba 软件** 是 Weibaba 所开发软件产品的作品集主站：汇总各产品官网入口，每款产品都有独立官网。

这里的每一款软件，都纯粹是因为爱好而开发——把平常经常遇到的需求，做成了一个个小工具。

![static](https://img.shields.io/badge/type-static-blue) ![zero-tracking](https://img.shields.io/badge/privacy-zero--tracking-green) ![zh/en](https://img.shields.io/badge/lang-zh%2Fen-yellow)

> 说明：徽章图为 shields.io 外链，仅用于 README 展示；站点页面本身零外部请求（站点红线见 `AGENTS.md`）。

## 产品列表

| 产品 | 中文名 | 状态 | 官网 |
|---|---|---|---|
| JustForShow | 做个样子 | 已发布 | <https://justforshow.weibaba.fun> |
| PassGone |  | 已发布 | <https://passgone.weibaba.fun> |
| PrivaMask | 数隐通 | 已发布 | <https://privamask.weibaba.fun> |
| ExifMate |  | 已发布 | <https://exifmate.weibaba.fun> |
| SourceLens | 源鉴 | 已发布 | <https://sourcelens.weibaba.fun> |
| ForceSplit |  | 已发布 | <https://forcesplit.weibaba.fun> |
| FinFlowScope |  | 开发中 | 即将推出 |

各产品功能特点与 logo 以主站主页为准；口径来源见 `docs/site-design.md` D3/D14。

## 关于本仓库

- 托管 Weibaba 软件产品主站（作品集入口），纯静态、零追踪、无 JavaScript。
- 站点结构与红线遵循 rules/release.md 9.3 与 rules/website.md；产品口径与设计决策以 `docs/site-design.md` 为准，口径变更先改文档再改代码。

## 站点结构

```text
main_website/
├── index.html              # 中文主站
├── en/                     # 英文版（含 en/privacy/）
├── privacy/                # 隐私政策（中文）
├── assets/
│   ├── style.css           # 全站唯一样式
│   └── img/                # weblogo.jpg（徽标源图）、weibaba_face.jpg（作者画像）、
│                           # donate_qr.jpg（收款码）、products/（各产品 logo）、
│                           # logo.png、og.png（派生）
├── favicon.ico | favicon.png | apple-touch-icon.png   # 均由 tools/make_icons.py 派生
├── robots.txt | sitemap.xml | _headers | .well-known/security.txt
├── tools/
│   ├── src/weblogo.jpg     # 图标派生源图（用户提供）
│   └── make_icons.py       # 图标生成脚本（唯一设计源头）
├── main_website.cmd        # 项目同名启动命令
├── docs/site-design.md     # 需求、设计与决策记录（含版本表）
└── README.md | README.en.md | AGENTS.md
```

## 本地运行

首选项目同名命令（全局第 16 条）：在项目根目录执行 `main_website.cmd`，自动使用 conda 环境 `main_website` 启动本地服务并打开 `http://127.0.0.1:8080/`；环境缺失时会提示创建 `conda create -n main_website python=3.13`。

补充方式：`conda run -n main_website --no-capture-output python -m http.server 8080 --bind 127.0.0.1`

## 仓库与提交规范

- 日常开发在 `dev` 分支；发布合入 `main` 并打轻量标签（全局第 3 条）。
- 提交信息只写版本号（如 `v1.2.0`），改动记录于 `docs/site-design.md` 版本表。
- NAS 推送不受限；GitHub 推送仅限网站仓库且地址须用户确认（全局 15.3）。

## 联系

联系与反馈：<feed@weibaba.fun>（请注明产品名称）

## 隐私

本站不收集任何数据：无统计、无 Cookie、无表单。详见[隐私政策](privacy/)；各产品隐私政策见其官网 `/privacy/` 页。

## 请作者喝咖啡

如果哪款小工具帮到了你，欢迎请作者喝杯咖啡 ☕

<p align="center"><img src="assets/img/donate_qr.jpg" alt="请作者喝咖啡收款码" width="230"></p>

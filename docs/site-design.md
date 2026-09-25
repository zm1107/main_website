# main_website 站点设计与决策记录

#文档 #决策记录 #官网 #主站

本文件是 Weibaba 软件主站的需求、设计与决策权威文档；口径变更必须先回写本文件再改代码（全局第 7 条文档驱动）。

## 需求

- 用户于 2026-09-26 提出主站需求：所开发的全部 app/软件项目统一在主站展示；展示内容包括各产品英文名、中文名与介绍。
- 列入七款：JustForShow（做个样子）、PassGone、PrivaMask（数隐通）、ExifMate、SourceLens（源鉴）、ForceSplit、FinFlowScope。其中 ForceSplit 与 FinFlowScope 为开发中（ForceSplit 状态来自其应用仓 README 权威口径）。
- 用户补充口径（2026-09-26 第二批）：域名确认为 `https://weibaba.fun`；批准读取各产品应用仓库与网站仓库取材；联系邮箱 `feed@weibaba.fun`（请注明产品名称）；加入「请作者喝咖啡」并在 GitHub README 同步；提供站点徽标图 `weblogo.jpg` 与作者头像 `weibaba_face.jpg`（原置于项目根，已移入 `assets/img/`）；关于作者文案口径「纯粹因为爱好而开发，把常遇到的需求做成小工具」；GitHub 已建仓，按规范推送。
- NAS 远程仓库（用户提供）：`ssh://git@nas.weibaba.life:53001/Weibaba-SoftWare/main_website.git`。
- 父目录 `D:\Weibaba-SoftWare\` 下的 Chronomark、LANsider、doc_cracker、stockprofile 暂不列入（用户口径，如需调整由用户明示）。

## 决策记录

- D1 域名（已确认）：`https://weibaba.fun/`，主域即主站，产品子站挂二级域名。
- D2 部署：NAS 推送不受限；GitHub 发布源按 rules/website.md 15.2 约定 `git@github.com:zm1107/main_website.git`，用户已确认建仓并授权按规范推送，推送前以 `git ls-remote` 验证地址有效。
- D3 取材（已授权）：产品口径来源——JustForShow / PassGone / PrivaMask / ExifMate 取自各自官网仓 `index.html` 与 `en/index.html` 的 og 口径（本地路径 `D:\github\<产品名>`）；SourceLens / ForceSplit 取自应用仓 `README.md` / `README.en.md`；功能特点取自各应用仓 README 的核心特性/主要功能清单（PassGone 为 README 标语行 + 官网英文版标题；ExifMate 为官网「四大核心卖点」）。ForceSplit 状态：**已发布**（用户口径 2026-09-26：「马上开发完毕，可以当作已发布」，覆盖其 README「尚未发布」旧状态）。FinFlowScope 暂无仓库，仅展示名称与「开发中」状态，不写介绍（全局第 5 条零编造）。
- D4 仓库结构：沿用 rules/release.md 9.3 网站仓库结构——`index.html` 中文主站、`en/` 英文版、`privacy/` 隐私页、`assets/style.css` 全站唯一样式、`assets/img/` 图像（weblogo.jpg、weibaba_face.jpg、donate_qr.jpg、logo.png、og.png）、`favicon.ico|.png`、`apple-touch-icon.png`、`robots.txt`、`sitemap.xml`、`_headers`、`.well-known/security.txt`、`README.md` + `README.en.md`、`AGENTS.md`、本设计文档、`tools/make_icons.py`（源图 `tools/src/weblogo.jpg`）。
- D5 分支与提交：按全局第 3 条，日常开发在 `dev`，发布合入 `main` 并打轻量标签；提交信息只写版本号，改动记录于本文件版本表。
- D6 运行方式：项目同名命令 `main_website.cmd`（全局第 16 条），使用同名 conda 环境 `main_website` 启动本地静态服务。
- D7 站点红线（硬性）：纯静态、零追踪——无统计/分析、无任何外部资源请求（无 CDN 字体、外链图片）、无 Cookie、无表单、无服务端代码、无 JavaScript；CSP 通过 `_headers` 全站收紧（README 中的 shields.io 徽章仅存在于 README，不入页面）。
- D8 提交身份：暂用全局身份 `Weibaba <zm1107@live.com>`；如需主站专属身份待用户提供。
- D9 联系方式（用户口径）：`feed@weibaba.fun`（请注明产品名称）；用于页脚、关于作者区、隐私页「联系方式」与 `.well-known/security.txt`。
- D10 请作者喝咖啡（用户口径）：收款码取自 justforshow 官网仓 `assets/img/donate_qr.jpg`（与 passgone 官网仓同图）。**弹出式**（用户口径 2026-09-26：不要直接展示，点击弹出图片）：交互参照 PassGone 样式（跳动咖啡按钮 + 点击弹收款码 + 遮罩/✕ 关闭），但以纯 CSS `:target` 弹层实现（`#qr-modal`），保持本仓「无 JavaScript」红线与 CSP 不变；`prefers-reduced-motion` 时停用跳动动画。GitHub README 内无法弹层，仍直接展示收款码。
- D11 视觉素材（用户提供）：`weblogo.jpg` 为站点徽标源图（1024×1024 白底圆形徽章 + Weibaba Zhang SoftWare 字样，源图存 `tools/src/`），favicon / apple-touch-icon / logo.png / og.png 全部由 `tools/make_icons.py` 从其派生（取徽章区域，禁止手改图片）；`weibaba_face.jpg` 为作者头像（油画风格双人像，含画框，完整展示、不做裁切）。
- D12 关于作者文案（用户口径扩写）：中文「这些软件都出自个人爱好。开发初衷很简单：日常里经常遇到的小需求，顺手把它们做成小工具。希望它们也能帮到你。」；英文对应翻译。
- D13 产品链接（用户口径 2026-09-26 第三批，覆盖各官网仓 canonical）：统一使用 `https://<项目名小写>.weibaba.fun`——JustForShow、PassGone（`passgone.weibaba.fun`，忽略其官网仓旧 canonical `passgone.exifmate.com`）、PrivaMask、ExifMate（`exifmate.weibaba.fun`，忽略旧 canonical `exifmate.com`）、ForceSplit、SourceLens；FinFlowScope 开发中暂不外链。
- D14 产品卡片信息结构（用户口径）：每款产品展示 **Logo + 英文名 + 中文名 + 干什么的（定位）+ 功能特点列表 + 官网链接**。产品 logo 入仓 `assets/img/products/<项目名小写>.png`，来源为各应用仓 `store/ico/app_icon.png` 源图标（ExifMate 用其官网仓 `assets/img/logo.png`，其应用仓不在本机）；功能特点为各仓权威清单的节选翻译对照，逐款来源见 D3。

## 待办与后续

1. FinFlowScope 上线后：补官网链接、中文名与介绍（以其应用仓为权威）。
2. ForceSplit 官网建成后：确认 `forcesplit.weibaba.fun` 可访问。
3. 主站专属 Git 提交身份（可选，待用户提供）。

## 版本表

- v1.0.0（2026-09-26）：初始骨架。中英双语主页与隐私页；七款产品入口卡片；图标脚本化派生；robots/sitemap/`_headers`/security.txt；README 双语；AGENTS.md；`main_website.cmd`；推送 NAS（dev、main、release/v1.0.0、标签 v1.0.0）。
- v1.1.0（2026-09-26）：域名确认 `weibaba.fun`；产品卡片补中文名与中英介绍（来源见 D3）；ForceSplit 修正为开发中且不外链；PassGone / ExifMate 链接按各官网仓 canonical 修正；新增「关于作者」（头像 + 爱好文案）与「请作者喝咖啡」（收款码）区块及页脚联系邮箱；隐私页与 security.txt 更新联系邮箱；徽标体系改为由用户提供的 `weblogo.jpg` 派生；README 双语加赞助区与关于作者；按规范推送 GitHub。
- v1.2.0（2026-09-26）：产品卡片升级为富卡片（Logo + 名称 + 中文名 + 定位 + 功能特点列表 + 官网链接，见 D14），六个产品 logo 入仓 `assets/img/products/`；ForceSplit 改「已发布」并外链（用户口径）；PassGone / ExifMate 链接统一为 `passgone.weibaba.fun` / `exifmate.weibaba.fun`（用户口径，覆盖旧 canonical）；README 产品表同步。
- v1.3.0（2026-09-26）：「请作者喝咖啡」改为弹出式收款码（纯 CSS `:target` 弹层：跳动咖啡按钮 + 遮罩 + ✕ 关闭，参照 PassGone 样式；无 JavaScript，页面不再直接展示收款码，见 D10）。

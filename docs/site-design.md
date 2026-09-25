# main_website 站点设计与决策记录

#文档 #决策记录 #官网 #主站

本文件是 Weibaba 软件主站的需求、设计与决策权威文档；口径变更必须先回写本文件再改代码（全局第 7 条文档驱动）。

## 需求

- 用户于 2026-09-26 提出主站需求：所开发的全部 app/软件项目统一在主站展示。
- 首批列入七款：JustForShow、PassGone、PrivaMask、ExifMate、ForceSplit、SourceLens（已发布），FinFlowScope（开发中）。
- NAS 远程仓库（用户提供）：`ssh://git@nas.weibaba.life:53001/Weibaba-SoftWare/main_website.git`。
- 父目录 `D:\Weibaba-SoftWare\` 下的 Chronomark、LANsider、doc_cracker、stockprofile 暂不列入（用户口径，如需调整由用户明示）。

## 决策记录

- D1 域名：默认采用 `https://weibaba.fun/`（主域即主站，产品子站按全局第 12 条挂二级域名）。依据全局第 12/15 条派生，**待用户最终确认**。
- D2 部署：v1.0.0 仅建站并推送 NAS；Cloudflare Pages / GitHub 发布源配置待用户提供仓库地址后进行。全局 15.3 红线：仓库地址不清楚必须询问用户，不得猜测或自动创建。
- D3 取材：未获用户批准前不读取各产品仓库（全局第 4 条），主站不写各产品功能简介，仅展示名称、状态与官网链接；链接按全局第 12 条 `<英文项目名小写>.weibaba.fun` 派生（JustForShow、PassGone、PrivaMask、ForceSplit、SourceLens 五款位于 `D:\Weibaba-SoftWare\`，口径直接适用）。ExifMate 不在该目录下，其链接 `https://exifmate.weibaba.fun` 依 rules/release.md 9.3 修正说明（新域名约定覆盖旧 `exifmate.com` 约定）派生，**待确认**。
- D4 仓库结构：沿用 rules/release.md 9.3 网站仓库结构——`index.html` 中文主站、`en/` 英文版、`privacy/` 隐私页、`assets/style.css` 全站唯一样式、`assets/img/` 图像、`favicon.ico|.png`、`apple-touch-icon.png`、`robots.txt`、`sitemap.xml`、`_headers`、`.well-known/security.txt`、`README.md` + `README.en.md`、`AGENTS.md`、本设计文档。图标全部由 `tools/make_icons.py` 脚本化派生，禁止手改。
- D5 分支与提交：按全局第 3 条，日常开发在 `dev`，发布合入 `main` 并打轻量标签；提交信息只写版本号，改动记录于本文件版本表（rules/release.md 9.3）。
- D6 运行方式：项目同名命令 `main_website.cmd`（全局第 16 条），使用同名 conda 环境 `main_website` 启动本地静态服务；命令缺失或环境缺失时按命令内提示修复。
- D7 站点红线（硬性，rules/release.md 9.3）：纯静态、零追踪——无统计/分析、无任何外部资源请求（无 CDN 字体、外链图片）、无 Cookie、无表单、无服务端代码；本站额外做到无 JavaScript。CSP 通过 `_headers` 全站收紧。
- D8 提交身份：暂用全局身份 `Weibaba <zm1107@live.com>`；若需主站专属身份（如 rules/release.md 9.3 的产品身份做法），待用户提供。

## 待确认清单（需用户口径后更新本文件与站点）

1. 主站域名是否为 `weibaba.fun`。
2. ExifMate 官网链接是否为 `https://exifmate.weibaba.fun`。
3. 各产品简介、图标、商店链接的取材授权（批准后从各应用仓库权威文件补齐，遵守全局第 5 条零编造）。
4. `.well-known/security.txt` 联系邮箱（当前为「示例 · 待替换」占位）。
5. GitHub 网站仓库地址与 Cloudflare Pages 配置（是否走 GitHub + Pages 发布）。
6. FinFlowScope 上线后的官网链接与简介。

## 版本表

- v1.0.0（2026-09-26）：初始骨架。中英双语主页与隐私页；七款产品入口卡片（六款已发布 + FinFlowScope 标注开发中）；图标由 `tools/make_icons.py` 派生（favicon.ico/png、apple-touch-icon、logo、og 图）；robots.txt、sitemap.xml、`_headers`、`.well-known/security.txt`；README 双语；AGENTS.md 仓库约束；`main_website.cmd` 同名命令；推送 NAS（dev、main、release/v1.0.0、标签 v1.0.0）。

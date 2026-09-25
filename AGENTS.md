# main_website 仓库约束

#AGENTS #规范 #官网

本仓库是 Weibaba 软件产品主站（网站仓库）。进入任何建站、改页、部署、推送工作前，必须先完整阅读并遵守 `C:\Users\weibaba\.zcode\rules\release.md`（9.3）与 `C:\Users\weibaba\.zcode\rules\website.md`（第 15 条），并遵循以下仓库级约束：

## 站点红线

- 纯静态、零追踪：无统计/分析、无任何外部资源请求（无 CDN 字体、外链图片）、无 Cookie、无表单、无服务端代码、无 JavaScript。
- 全站唯一样式文件为 `assets/style.css`，不得引入第二样式文件或内联样式。
- 仓库不得出现用户数据、操作日志、凭据、本机路径等任何非公开信息。

## 口径管理

- 各产品名称、简介、链接等口径只能来自用户提供的口径或对应应用仓库的权威文件（README、store/、docs/、PRIVACY.md），禁止凭记忆生成。
- 当前版本产品链接按全局第 12 条 `<英文项目名小写>.weibaba.fun` 派生；ExifMate 链接待确认（见 `docs/site-design.md` 待确认清单）。
- 任何口径变更先回写 `docs/site-design.md` 再改代码。

## 图标派生

- `favicon.ico`、`favicon.png`、`apple-touch-icon.png`、`assets/img/logo.png`、`assets/img/og.png` 全部由 `tools/make_icons.py` 生成，禁止手工修改图片文件。

## 提交与分支

- 日常开发在 `dev` 分支；发布流程遵循全局第 3 条与 rules/release.md 9.4。
- 提交信息只写版本号（如 `v1.2.0`），不写改动说明；改动内容记录于 `docs/site-design.md` 版本表。

## 推送限制

- NAS 远程（`ssh://git@nas.weibaba.life:53001/Weibaba-SoftWare/main_website.git`）推送不受限。
- GitHub 推送仅允许网站仓库，且仓库地址必须由用户提供，不得猜测或自动创建（全局 15.3）；推送前按站点红线自检。

## 运行方式

- 默认通过项目同名命令 `main_website.cmd` 运行/验证/演示（全局第 16 条）；环境缺失时按命令内提示修复，不得绕开。

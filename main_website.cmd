@echo off
setlocal
chcp 65001 >nul
cd /d "%~dp0"

where conda >nul 2>nul
if errorlevel 1 (
  echo [错误] 未找到 conda 命令。请先安装并初始化 conda，再运行本命令。
  exit /b 1
)

conda env list | findstr /B /C:"main_website " >nul 2>nul
if errorlevel 1 (
  echo [提示] 未找到 conda 环境 main_website，正在自动创建（python=3.13）……
  conda create -n main_website python=3.13 -y
  if errorlevel 1 (
    echo [错误] 环境创建失败。请手动执行：conda create -n main_website python=3.13
    exit /b 1
  )
)

if not "%~1"=="--no-open" start "" http://127.0.0.1:8080/
echo 正在启动本地站点服务：http://127.0.0.1:8080/  （关闭本窗口或按 Ctrl+C 停止）
conda run -n main_website --no-capture-output python -m http.server 8080 --bind 127.0.0.1

# Sudoku Mansion 1.3.1 简体中文汉化安装
# 双击本文件即可运行（或在 PowerShell 中执行）
$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $here

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) { $python = Get-Command py -ErrorAction SilentlyContinue }
if (-not $python) {
  Write-Host '未找到 python，请安装 Python 3，或改用命令行指定解释器运行 install.py。' -ForegroundColor Red
  Read-Host '按回车键退出'
  exit 1
}

& $python.Source install.py @args
$code = $LASTEXITCODE
Write-Host ''
Read-Host '按回车键关闭窗口'
exit $code

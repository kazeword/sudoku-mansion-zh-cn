# Sudoku Mansion 简体中文汉化 · 还原英文（1.3.2 适配版）
# 双击本文件即可运行；也可在 PowerShell 中执行 python restore.py
$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $here

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) { $python = Get-Command py -ErrorAction SilentlyContinue }
if (-not $python) {
  Write-Host '未找到 python，请先安装 Python 3，或手动执行：python restore.py' -ForegroundColor Red
  Read-Host '按回车键退出'
  exit 1
}

& $python.Source restore.py @args
$code = $LASTEXITCODE
Write-Host ''
Read-Host '按回车键关闭窗口'
exit $code

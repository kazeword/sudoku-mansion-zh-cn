# -*- coding: utf-8 -*-
"""把仓库结构组装成可发布的汉化包，并生成 Releases 压缩包。

用法：
    python tools/build_package.py

流程：
    package/ 源码  ──复制──▶  build/<包名>/  ──zip──▶  dist/<包名>.zip
生成过程中会调用 package/make_patch.py，用官方 1.2.7 数据 + 1.3.x 新增译文
重新生成 zh-cn-patch.js 与 translations.json。
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PACKAGE = os.path.join(ROOT, "package")
BUILD = os.path.join(ROOT, "build")
DIST = os.path.join(ROOT, "dist")
SOURCE_PATCH = os.path.join(ROOT, ".source", "patch")

PACKAGE_SRC = [
    "install.py", "restore.py", "verify.py", "make_patch.py", "zh_cn_data.py",
    "zh-cn-patch.template.js", "zh-cn-patch.css", "installed.json.example",
    "README.md", "LICENSE", "THIRD-PARTY-NOTICES.md",
    "安装汉化.ps1", "还原英文.ps1",
]
TOOLS_SRC = ["build_release.py", "merge_translation_data.py"]


def copy_files(files, src_dir, dst_dir):
    os.makedirs(dst_dir, exist_ok=True)
    for f in files:
        src = os.path.join(src_dir, f)
        if not os.path.isfile(src):
            raise SystemExit(f"缺少文件：{src}")
        shutil.copy2(src, os.path.join(dst_dir, f))


def main():
    if not os.path.isdir(SOURCE_PATCH):
        raise SystemExit(
            f"找不到官方 1.2.7 汉化数据：{SOURCE_PATCH}\n"
            "请把官方汉化包的 patch 文件夹放到 .source/patch 后重试。")

    # 1. 清空并复制包内容
    pkg_dir = os.path.join(BUILD, "Sudoku-Mansion-zh-CN")
    shutil.rmtree(pkg_dir, ignore_errors=True)
    copy_files(PACKAGE_SRC, PACKAGE, pkg_dir)
    copy_files(TOOLS_SRC, HERE, os.path.join(pkg_dir, "tools"))

    # 2. 用官方数据 + 新译文重新生成汉化数据
    subprocess.run([sys.executable, os.path.join(pkg_dir, "make_patch.py"),
                    "--source-patch", SOURCE_PATCH, "--out", pkg_dir], check=True)

    # 3. 生成 Releases 压缩包
    os.makedirs(DIST, exist_ok=True)
    subprocess.run([sys.executable, os.path.join(pkg_dir, "tools", "build_release.py"),
                    "--out-dir", DIST], check=True)

    # 4. 写出校验和
    meta = json.load(open(os.path.join(pkg_dir, "translations.json"), encoding="utf-8"))
    zip_path = os.path.join(DIST, f"Sudoku-Mansion-zh-CN-{meta['patchVersion']}.zip")
    digest = hashlib.sha256(open(zip_path, "rb").read()).hexdigest()
    with open(zip_path + ".sha256", "w", encoding="utf-8", newline="\n") as f:
        f.write(f"{digest}  {os.path.basename(zip_path)}\n")
    print(f"SHA256: {digest}")
    print(f"发布包目录: {pkg_dir}")
    print(f"发布压缩包: {zip_path}")


if __name__ == "__main__":
    sys.exit(main())

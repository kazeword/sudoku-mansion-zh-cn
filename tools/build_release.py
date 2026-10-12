# -*- coding: utf-8 -*-
"""生成发布用压缩包（Releases 附件）。

用法：
    python build_release.py [--out-dir dist]

产物：dist/Sudoku-Mansion-zh-CN-<版本>.zip
解压后即得到可直接运行的汉化包（含安装/还原脚本与汉化数据）。
"""
import argparse
import json
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def find_package_dir():
    """仓库布局返回 ../package，打包后的布局返回 tools 的上级目录。"""
    repo_pkg = os.path.join(ROOT, "package")
    if os.path.isdir(repo_pkg):
        return repo_pkg
    if os.path.basename(HERE) == "tools":
        return ROOT
    return HERE

PACKAGE_FILES = [
    "install.py",
    "restore.py",
    "verify.py",
    "installed.json.example",
    "translations.json",
    "zh-cn-patch.js",
    "zh-cn-patch.template.js",
    "zh-cn-patch.css",
    "README.md",
    "安装汉化-1.3.2.ps1",
    "还原英文-1.3.2.ps1",
    "LICENSE",
    "THIRD-PARTY-NOTICES.md",
    "tools/build_release.py",
    "tools/merge_translation_data.py",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default=os.path.join(ROOT, "dist"))
    args = ap.parse_args()

    meta = json.load(open(os.path.join(find_package_dir(), "translations.json"), encoding="utf-8"))
    version = meta["patchVersion"]
    game_version = meta["gameVersion"]
    name = f"Sudoku-Mansion-zh-CN-{version}"
    os.makedirs(args.out_dir, exist_ok=True)
    zip_path = os.path.join(args.out_dir, name + ".zip")

    pkg = find_package_dir()
    missing = [f for f in PACKAGE_FILES if not os.path.isfile(os.path.join(pkg, f))]
    if missing:
        raise SystemExit("缺少发布文件：" + ", ".join(missing))

    version_txt = (
        f"汉化版本: {version}\n"
        f"适用游戏版本: {game_version}\n"
        f"文本翻译条目: {len(meta['entries'])}\n"
        f"基于: {meta['basedOn']}\n"
    )

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for f in PACKAGE_FILES:
            z.write(os.path.join(pkg, f), os.path.join(name, f))
        z.writestr(os.path.join(name, "VERSION.txt"), version_txt)

    size = os.path.getsize(zip_path)
    print(f"已生成: {zip_path}  ({size/1024:.1f} KiB)")
    print(f"包含文件: {len(PACKAGE_FILES) + 1}")


if __name__ == "__main__":
    sys.exit(main())

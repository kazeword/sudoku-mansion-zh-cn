# -*- coding: utf-8 -*-
"""Sudoku Mansion 汉化还原脚本（配合 1.3.1 适配版安装脚本使用）。

用法：
    python restore.py            # 还原最近一次安装前的英文原文件
    python restore.py --list     # 查看可用的备份
"""
import argparse
import json
import os
import shutil
import sys
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--game-root", default=None)
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--manifest", default=None, help="安装记录位置（默认：本脚本所在目录）")
    args = ap.parse_args()

    manifest_path = args.manifest or os.path.join(HERE, "installed.json")
    if not os.path.isfile(manifest_path):
        raise SystemExit(f"找不到安装记录：{manifest_path}；请手动从备份目录还原。")
    manifest = json.load(open(manifest_path, encoding="utf-8"))
    backup = manifest["backupDir"]

    if args.list:
        print("上次安装记录：")
        for label, info in manifest["files"].items():
            print(f"  {label}: {info['path']}")
        print(f"备份目录: {backup}")
        return

    if not os.path.isdir(backup):
        raise SystemExit(f"备份目录不存在：{backup}")

    browser = os.path.dirname(manifest["files"]["index"]["path"])
    resources = os.path.dirname(os.path.dirname(os.path.dirname(browser)))
    originals = os.path.join(backup, "originals")
    front_dest = os.path.join(browser, "assets", "mansion.json")
    back_dest = os.path.join(resources, "backend", "data", "mansions", "mansion_default.json")
    mapping = {
        "frontendJson": ("mansion.json.frontendJson", front_dest),
        "backendJson": ("mansion_default.json.backendJson", back_dest),
        "index": ("index.html.index", os.path.join(browser, "index.html")),
    }
    print(f"游戏资源目录: {resources}")

    for label, (backup_name, dest) in mapping.items():
        src = os.path.join(originals, backup_name)
        if not os.path.isfile(src):
            raise SystemExit(f"备份文件缺失：{src}")
        shutil.copy2(src, dest)
        print(f"已还原：{dest}")

    for extra in ("zh-cn-patch.js", "zh-cn-patch.css"):
        p = os.path.join(browser, extra)
        if os.path.isfile(p):
            os.remove(p)
            print(f"已删除：{p}")

    manifest["restoredAt"] = datetime.now().strftime("%Y%m%d-%H%M%S")
    json.dump(manifest, open(manifest_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("\n已恢复英文原文件。请从 Steam 正常启动游戏。")
    print("（如果 Steam 之后更新过游戏，请改用 Steam 的“验证游戏文件完整性”。）")


if __name__ == "__main__":
    sys.exit(main())

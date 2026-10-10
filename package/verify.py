# -*- coding: utf-8 -*-
"""安装结果自检。

    python verify.py [--game-root <游戏目录>] [--manifest <installed.json>]

有安装记录时会校验：
    1. 汉化文件是否就位；
    2. 备份是否为可用的、与当前（已汉化）文件不同的原文件；
    3. 两个文本文件能否解析、是否已无残留英文；
    4. index.html 的 lang / 标题 / 脚本注入是否正确。
"""
import argparse
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FIELDS = {"name", "title", "description", "text", "rules", "hint", "label",
          "canvasTutorial", "roomCanvasTutorial", "unlockPopupText"}
MEDIA_RE = re.compile(r"\.(?:images|audio)\[\d+\]$")

ok = True


def check(label, cond, extra=""):
    global ok
    print(("  OK   " if cond else "  FAIL ") + label + (f"  {extra}" if extra else ""))
    if not cond:
        ok = False


def find_game_root(explicit=None):
    if explicit:
        return os.path.abspath(explicit)
    for drive in ("C:", "D:", "E:", "F:", "G:"):
        for sub in (r"steam\steamapps\common\Sudoku Mansion",
                    r"SteamLibrary\steamapps\common\Sudoku Mansion",
                    r"Program Files (x86)\Steam\steamapps\common\Sudoku Mansion",
                    r"Program Files\Steam\steamapps\common\Sudoku Mansion"):
            p = os.path.join(drive + "\\", sub)
            if os.path.isfile(os.path.join(p, "Sudoku Mansion.exe")):
                return p
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--game-root", default=None)
    ap.add_argument("--manifest", default=os.path.join(HERE, "installed.json"))
    args = ap.parse_args()

    manifest = None
    if os.path.isfile(args.manifest):
        manifest = json.load(open(args.manifest, encoding="utf-8"))
        browser_hint = os.path.dirname(manifest["files"]["index"]["path"])
        # <游戏目录>\resources\frontend\dist\browser -> <游戏目录>
        game_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(browser_hint))))
        print(f"安装记录: {args.manifest}")
    else:
        game_root = find_game_root(args.game_root)
        if not game_root:
            raise SystemExit("未找到游戏目录，请用 --game-root 指定。")
        print("未找到安装记录，仅做基础检查。")

    resources = os.path.join(game_root, "resources")
    browser = os.path.join(resources, r"frontend\dist\browser")
    front = os.path.join(browser, r"assets\mansion.json")
    back = os.path.join(resources, r"backend\data\mansions\mansion_default.json")
    index = os.path.join(browser, "index.html")
    print(f"游戏目录: {game_root}\n")

    print("== 1. 汉化文件 ==")
    for f in (index, front, back, os.path.join(browser, "zh-cn-patch.js"),
              os.path.join(browser, "zh-cn-patch.css")):
        check(os.path.relpath(f, game_root), os.path.isfile(f))

    if manifest:
        print("\n== 2. 备份可用性 ==")
        backup = manifest.get("backupDir")
        check("备份目录存在", os.path.isdir(backup or ""), backup or "")
        if os.path.isdir(backup or ""):
            originals = os.path.join(backup, "originals")
            for name, dest in (("index.html.index", index),
                               ("mansion.json.frontendJson", front),
                               ("mansion_default.json.backendJson", back)):
                src = os.path.join(originals, name)
                if not os.path.isfile(src):
                    check(f"备份 {name}", False)
                    continue
                same = (hashlib.sha256(open(src, "rb").read()).hexdigest() ==
                        hashlib.sha256(open(dest, "rb").read()).hexdigest())
                check(f"备份 {name} 可还原（与当前已汉化文件不同）", not same)

    print("\n== 3. 文本文件 ==")
    for label, path in (("frontend/mansion.json", front), ("backend/mansion_default.json", back)):
        if not os.path.isfile(path):
            check(f"{label} 存在", False)
            continue
        try:
            data = json.load(open(path, encoding="utf-8"))
            parsed = True
        except Exception as e:
            parsed = False
            print("     JSON 解析错误:", e)
        check(f"{label} JSON 可解析", parsed)
        if not parsed:
            continue
        left = []

        def walk(n, p):
            if isinstance(n, list):
                for i, v in enumerate(n):
                    walk(v, f"{p}[{i}]")
            elif isinstance(n, dict):
                for k, v in n.items():
                    if isinstance(v, str) and k in FIELDS and not (k == "name" and MEDIA_RE.search(p)):
                        if re.search(r"[A-Za-z]{4,}", v) and not re.search(r"[\u4e00-\u9fff]", v):
                            left.append(v)
                    else:
                        walk(v, f"{p}.{k}")

        walk(data, "$")
        check(f"{label} 无残留英文文本", len(left) == 0,
              f"残留 {len(left)}" + (f": {left[0][:60]!r}" if left else ""))
        if data.get("rooms"):
            print(f"     示例: {data['rooms'][0].get('name', '')!r}")

    print("\n== 4. index.html 入口 ==")
    if os.path.isfile(index):
        idx = open(index, encoding="utf-8").read()
        m = re.search(r"<title>(.*?)</title>", idx)
        check("lang 为 zh-CN", '<html lang="zh-CN"' in idx)
        check("标题已汉化", bool(m) and "数独庄园" in m.group(1), m.group(1) if m else "")
        check("已挂载 zh-cn-patch.js", "zh-cn-patch.js" in idx)
        check("已挂载 zh-cn-patch.css", "zh-cn-patch.css" in idx)
        check("未重复注入", idx.count("zh-cn-patch.js") == 1)
        poly = re.search(r"polyfills-[^\"']+\.js", idx)
        if poly:
            check("汉化脚本在模块入口之前", idx.index("zh-cn-patch.js") < poly.start())

    print("\n结果:", "全部通过" if ok else "存在问题")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

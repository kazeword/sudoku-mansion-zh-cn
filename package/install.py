# -*- coding: utf-8 -*-
"""Sudoku Mansion 1.3.1 简体中文汉化安装脚本（适配版）

用法（在 PowerShell 中）：
    python install.py                # 安装
    python install.py --dry-run      # 只检查，不修改任何文件
    python install.py --game-root "D:\\SteamLibrary\\steamapps\\common\\Sudoku Mansion"
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
REQUIRED_VERSION = "1.3.2"
FIELDS = ("name", "title", "description", "text", "rules", "hint", "label",
          "canvasTutorial", "roomCanvasTutorial", "unlockPopupText")
MEDIA_RE = re.compile(r"\.(?:images|audio)\[\d+\]$")

STEAM_APP_ID = 5005590


def find_game_root(explicit=None):
    candidates = []
    if explicit:
        candidates.append(explicit)
    for drive in ("C:", "D:", "E:", "F:", "G:"):
        candidates.append(f"{drive}\\steam\\steamapps\\common\\Sudoku Mansion")
        candidates.append(f"{drive}\\SteamLibrary\\steamapps\\common\\Sudoku Mansion")
        candidates.append(f"{drive}\\Program Files (x86)\\Steam\\steamapps\\common\\Sudoku Mansion")
        candidates.append(f"{drive}\\Program Files\\Steam\\steamapps\\common\\Sudoku Mansion")
    for c in candidates:
        if c and os.path.isfile(os.path.join(c, "Sudoku Mansion.exe")):
            return os.path.abspath(c)
    raise SystemExit("未找到《Sudoku Mansion》安装目录，请用 --game-root 指定。")


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_json(path):
    """读 JSON：兼容带 BOM 的文件。"""
    with open(path, encoding="utf-8-sig") as f:
        return json.load(f)


def write_json(path, data):
    """写 JSON：UTF-8 无 BOM，避免部分工具写入 BOM 后解析失败。"""
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def load_translations():
    path = os.path.join(HERE, "translations.json")
    data = read_json(path)
    return {e["hash"]: e["target"] for e in data["entries"]}, data


def patch_json_text(text, table, field):
    """Replace JSON string values of `field` using the hash lookup.

    Works on the raw text so the original formatting/escaping is preserved.
    """
    counter = [0]

    def repl(m):
        english = json.loads(m.group(4))          # group(4) is the literal, with quotes
        target = table.get(sha256_text(english))
        if target is None:
            return m.group(0)
        counter[0] += 1
        escaped = json.dumps(target, ensure_ascii=False)
        return m.group(1) + ':' + m.group(2) + escaped

    pattern = re.compile(r'("' + field + r'")' + r'(\s*):(\s*)("(?:[^"\\]|\\.)*")')
    new_text = pattern.sub(repl, text)
    return new_text, counter[0]


def escaped_value_variants(value):
    a = json.dumps(value, ensure_ascii=False)
    b = json.dumps(value, ensure_ascii=True)
    return {a, b}


def apply_translations(text, table):
    """Apply every translatable field to the raw JSON text; returns (text, count)."""
    total = 0
    for field in FIELDS:
        text, c = patch_json_text(text, table, field)
        total += c
    return text, total


def dry_run_report(game_root, table):
    browser = os.path.join(game_root, "resources", "frontend", "dist", "browser")
    files = [
        os.path.join(browser, "assets", "mansion.json"),
        os.path.join(game_root, "resources", "backend", "data", "mansions", "mansion_default.json"),
        os.path.join(browser, "index.html"),
    ]
    print(f"游戏目录: {game_root}")
    for f in files:
        print(f"  [存在] {f}" if os.path.isfile(f) else f"  [缺失] {f}")
    found = 0
    for f in files[:2]:
        text = open(f, encoding="utf-8").read()
        _, total = apply_translations(text, table)
        found += total
        print(f"  可替换文本数: {total}  ({os.path.basename(f)})")
    print(f"合计将替换 {found} 处文本（两种文件合计）。")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--game-root", default=None)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--manifest", default=None,
                    help="安装记录写入位置（默认：本脚本所在目录）")
    args = ap.parse_args()

    manifest_path = args.manifest or os.path.join(HERE, "installed.json")

    table, meta = load_translations()
    print(f"汉化数据版本: {meta['patchVersion']}（适用游戏 {meta['gameVersion']}）")
    print(f"翻译条目: {len(table)}")

    target_version = meta["gameVersion"]

    game_root = find_game_root(args.game_root)
    exe = os.path.join(game_root, "Sudoku Mansion.exe")
    ver = None
    try:
        import subprocess
        out = subprocess.run(
            ["powershell", "-NoProfile", "-Command",
             f"(Get-Item -LiteralPath '{exe}').VersionInfo.FileVersion"],
            capture_output=True, text=True)
        ver = (out.stdout or "").strip()
    except Exception:
        pass
    print(f"游戏版本: {ver or '未知'}")

    resources = os.path.join(game_root, "resources")
    browser = os.path.join(resources, "frontend", "dist", "browser")
    index_path = os.path.join(browser, "index.html")
    front_json = os.path.join(browser, "assets", "mansion.json")
    back_json = os.path.join(resources, "backend", "data", "mansions", "mansion_default.json")

    for p in (index_path, front_json, back_json):
        if not os.path.isfile(p):
            raise SystemExit(f"缺少游戏文件：{p}")

    index = open(index_path, encoding="utf-8").read()
    already = "zh-cn-patch.js" in index

    if args.dry_run:
        dry_run_report(game_root, table)
        if already:
            print("\n注意：入口文件里已经存在汉化脚本（可能已经装过汉化）。")
        print("\n[dry-run] 未修改任何文件。")
        return

    # ---- 1. 逐文件应用翻译 ----
    results = {}
    for label, path in (("frontendJson", front_json), ("backendJson", back_json)):
        text = open(path, encoding="utf-8").read()
        new_text, total = apply_translations(text, table)
        if total == 0:
            if already:
                raise SystemExit("检测到汉化已经安装（游戏文本中已无待翻译的英文原文）。\n"
                                 "如需重新安装，请先运行 python restore.py 还原英文。")
            raise SystemExit(f"文本匹配为 0：{path}。游戏文件可能已更新，请先验证游戏文件完整性。")
        results[label] = {"path": path, "replacements": total, "new_text": new_text}
        print(f"  文本替换 {total} 处 -> {os.path.basename(path)}")

    matches = results["frontendJson"]["replacements"] + results["backendJson"]["replacements"]
    if ver and not (ver == target_version or ver.startswith(target_version + ".")):
        print(f"!! 提示：本汉化按游戏 {target_version} 制作，当前版本为 {ver}。")
        print(f"!! 已成功匹配 {matches} 处文本，可以继续安装；如出现中英混杂属正常现象。")

    # ---- 2. index.html ----
    if already:
        print("检测到入口已注入汉化脚本，继续覆盖安装。")
    new_index = index.replace('<html lang="en"', '<html lang="zh-CN"', 1)
    new_index = new_index.replace("<title>Sudoku Mansion</title>", "<title>数独庄园</title>", 1)
    if "zh-cn-patch.css" not in new_index:
        new_index = new_index.replace(
            '<link rel="icon" type="image/x-icon" href="favicon.ico">',
            '<link rel="icon" type="image/x-icon" href="favicon.ico">\n    <link rel="stylesheet" href="zh-cn-patch.css">', 1)
    if "zh-cn-patch.js" not in new_index:
        new_index, n = re.subn(
            r'<script src="(polyfills-[^"]+\.js)" type="module"></script>',
            r'<script src="zh-cn-patch.js"></script><script src="\1" type="module"></script>',
            new_index, count=1)
        if n == 0:
            m = re.search(r'<script src="([^"]+\.js)"\s+type="module"></script>', new_index)
            if not m:
                raise SystemExit("无法把汉化脚本加入 index.html（未找到模块入口脚本）。")
            new_index = new_index[:m.start()] + '<script src="zh-cn-patch.js"></script>' + new_index[m.start():]
    if "zh-cn-patch.js" not in new_index or "zh-cn-patch.css" not in new_index:
        raise SystemExit("入口文件注入失败。")
    results["index"] = {"path": index_path, "new_text": new_index}

    # ---- 3. 备份 ----
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = os.path.join(resources, f"zh-cn-backup-{target_version}-adapted-{stamp}")
    os.makedirs(os.path.join(backup, "originals"), exist_ok=True)
    for label, info in results.items():
        shutil.copy2(info["path"], os.path.join(backup, "originals", os.path.basename(info["path"]) + f".{label}"))
    for extra in ("zh-cn-patch.js", "zh-cn-patch.css"):
        dst = os.path.join(browser, extra)
        if os.path.isfile(dst):
            shutil.copy2(dst, os.path.join(backup, "originals", extra))

    # ---- 4. 写入 ----
    for label in ("frontendJson", "backendJson", "index"):
        info = results[label]
        with open(info["path"], "w", encoding="utf-8", newline="") as f:
            f.write(info["new_text"])
    shutil.copy2(os.path.join(HERE, "zh-cn-patch.js"), os.path.join(browser, "zh-cn-patch.js"))
    shutil.copy2(os.path.join(HERE, "zh-cn-patch.css"), os.path.join(browser, "zh-cn-patch.css"))

    manifest = {
        "patchVersion": meta["patchVersion"],
        "gameVersion": ver or meta["gameVersion"],
        "targetGameVersion": meta["gameVersion"],
        "installedAt": stamp,
        "backupDir": backup,
        "files": {label: {"path": info["path"],
                          "replacements": info.get("replacements"),
                          "sha256After": hashlib.sha256(open(info["path"], "rb").read()).hexdigest()}
                  for label, info in results.items()},
    }
    write_json(manifest_path, manifest)

    print()
    print(f"《Sudoku Mansion》简体中文汉化（{meta['patchVersion']}）安装完成。")
    print(f"文本替换合计：{matches} 处")
    print(f"原文件备份：{backup}")
    print("如需还原英文，运行：python restore.py")
    print("请从 Steam 正常启动游戏。")


if __name__ == "__main__":
    sys.exit(main())

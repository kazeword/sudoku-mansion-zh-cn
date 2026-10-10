# -*- coding: utf-8 -*-
"""检查当前游戏文本与汉化数据的差距，并生成待补译清单。

用法：
    # 1) 报告：列出游戏里还没有译文、或译文已失效的文本
    python merge_translation_data.py --game-root "F:\\steam\\steamapps\\common\\Sudoku Mansion"

    # 2) 把补好译文的 JSON 合并回 zh_cn_data.py
    python merge_translation_data.py --apply-json <新译文.json>
    python merge_translation_data.py --apply-ui <新译文.json>

`--game-root` 省略时会尝试自动定位 Steam 游戏目录。
新译文文件格式（报告里的 missingJsonText 就是）：
    { "英文原文": "中文译文", ... }

注意：报告只统计"已失效或从未翻译"的文本；上游 1.2.7 的译文通过
package/translations.json 反查（哈希 -> 原文无法反查，因此报告以
`zh_cn_data` 与本次安装实际匹配的字符串为基线）。
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import zh_cn_data as D  # noqa: E402

FIELDS = ("name", "title", "description", "text", "rules", "hint", "label",
          "canvasTutorial", "roomCanvasTutorial", "unlockPopupText")
MEDIA_RE = re.compile(r"\.(?:images|audio)\[\d+\]$")


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
    raise SystemExit("未找到游戏目录，请用 --game-root 指定。")


def collect_json_strings(path):
    data = json.load(open(path, encoding="utf-8"))
    out = []

    def walk(node, p):
        if isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{p}[{i}]")
        elif isinstance(node, dict):
            for k, v in node.items():
                if isinstance(v, str) and k in FIELDS and not (k == "name" and MEDIA_RE.search(p)):
                    out.append((v, f"{p}.{k}"))
                else:
                    walk(v, f"{p}.{k}")

    walk(data, "$")
    return out


def unescape_js(s):
    out, i = [], 0
    m = {"n": "\n", "t": "\t", "r": "\r", "\\": "\\", "'": "'", '"': '"', "/": "/", "b": "\b", "f": "\f", "0": "\0"}
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s):
            n = s[i + 1]
            if n in m:
                out.append(m[n]); i += 2; continue
            if n in "ux":
                w = 4 if n == "u" else 2
                try:
                    out.append(chr(int(s[i + 2:i + 2 + w], 16))); i += 2 + w; continue
                except ValueError:
                    out.append(n); i += 2; continue
            out.append(n); i += 2; continue
        out.append(c); i += 1
    return "".join(out)


def report(game_root, out_path):
    resources = os.path.join(game_root, "resources")
    browser = os.path.join(resources, r"frontend\dist\browser")
    files = [os.path.join(browser, r"assets\mansion.json"),
             os.path.join(resources, r"backend\data\mansions\mansion_default.json")]

    known = set(D.JSON_NEW)
    missing = {}
    for f in files:
        for value, path in collect_json_strings(f):
            if value in known or not re.search(r"[A-Za-z]{3,}", value):
                continue
            missing.setdefault(value, path)

    LIT = re.compile(r'"((?:[^"\\]|\\.)*)"|\'((?:[^\'\\]|\\.)*)\'', re.S)
    ui_missing = {}
    for name in sorted(os.listdir(browser)):
        if not name.endswith(".js"):
            continue
        text = open(os.path.join(browser, name), encoding="utf-8", errors="replace").read()
        for a, b in LIT.findall(text):
            s = unescape_js(a if a else b)
            if s in D.UI_NEW:
                continue
            if len(s) < 4 or len(s) > 200 or not re.search(r"[A-Za-z]", s):
                continue
            if len(re.findall(r"[A-Za-z]", s)) / len(s) < 0.5 or " " not in s.strip():
                continue
            if not (s[0].isupper() or s[0].isdigit()):
                continue
            if re.search(r"(^M[\d. ]+[LHVQAZmhvqaz]|InjectorError|Observable|Promise|Zone|\[class\.|%COMP%)", s):
                continue
            ui_missing.setdefault(s, name)

    report_data = {
        "gameRoot": game_root,
        "missingJsonText": missing,
        "missingUiStrings": ui_missing,
    }
    json.dump(report_data, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    print(f"游戏目录: {game_root}")
    print(f"未被本补丁翻译过的文本（JSON）: {len(missing)} 条"
          "  ← 注意：这里包含上游 1.2.7 已翻译但本版未收录对照表的条目")
    for i, (k, v) in enumerate(list(missing.items())[:10], 1):
        print(f"  {i}. [{v}] {k[:80]!r}")
    print(f"未被本补丁翻译过的界面字符串: {len(ui_missing)} 条")
    for i, k in enumerate(list(ui_missing)[:10], 1):
        print(f"  {i}. {k!r}")
    print(f"\n完整清单已写入: {out_path}")
    print("补好译文后，用 --apply-json / --apply-ui 合并回 zh_cn_data.py。")


def _append_pairs(attr, pairs):
    path = os.path.join(HERE, "zh_cn_data.py")
    text = open(path, encoding="utf-8").read()
    marker = f"{attr} = {{"
    idx = text.index(marker)
    end = text.index("\n}", idx)
    blocks = []
    for k, v in pairs.items():
        blocks.append('\n    """%s""":\n    """%s""",'
                      % (k.replace("\\", "\\\\").replace('"""', '\\"\\"\\"'),
                         v.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')))
    text = text[:end] + "".join(blocks) + text[end:]
    open(path, "w", encoding="utf-8", newline="\n").write(text)
    print(f"已向 {attr} 追加 {len(pairs)} 条译文 -> {path}")
    print("请重新运行 tools/build_package.py 生成新的汉化数据。")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--game-root", default=None)
    ap.add_argument("--out", default=os.path.join(HERE, "todo-translations.json"))
    ap.add_argument("--apply-json", default=None, help="把 JSON 新译文合并进 zh_cn_data.py")
    ap.add_argument("--apply-ui", default=None, help="把界面新译文合并进 zh_cn_data.py")
    args = ap.parse_args()

    if args.apply_json or args.apply_ui:
        src = args.apply_json or args.apply_ui
        pairs = json.load(open(src, encoding="utf-8"))
        if not isinstance(pairs, dict):
            raise SystemExit("新译文文件必须是 { 原文: 译文 } 形式的 JSON 对象。")
        _append_pairs("JSON_NEW" if args.apply_json else "UI_NEW", pairs)
        return

    report(find_game_root(args.game_root), args.out)


if __name__ == "__main__":
    sys.exit(main())

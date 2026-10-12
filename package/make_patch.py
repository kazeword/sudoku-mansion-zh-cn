# -*- coding: utf-8 -*-
"""把官方 1.2.7 汉化数据与 1.3.x 新增译文合并，生成发布用的汉化数据。

用法：
    python make_patch.py --source-patch <官方 1.2.7 补丁的 patch 目录> [--out <输出目录>]

`--source-patch` 指向官方汉化包中的 patch 文件夹（内含 zh-cn-patch.js 与 translations.json），
默认在本目录的 .source/patch 下查找。
"""
import argparse
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import zh_cn_data as D


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


def js_quote(s):
    return ('"' + s.replace("\\", "\\\\").replace('"', '\\"')
            .replace("\n", "\\n").replace("\r", "\\r").replace("\t", "\\t") + '"')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-patch", default=os.path.join(HERE, ".source", "patch"),
                    help="官方 1.2.7 汉化包的 patch 目录")
    ap.add_argument("--out", default=HERE, help="输出目录（默认：本目录）")
    ap.add_argument("--patch-version", default="1.3.2-zh-cn.1")
    ap.add_argument("--game-version", default="1.3.2")
    args = ap.parse_args()

    src_js_path = os.path.join(args.source_patch, "zh-cn-patch.js")
    src_trans_path = os.path.join(args.source_patch, "translations.json")
    for p in (src_js_path, src_trans_path):
        if not os.path.isfile(p):
            raise SystemExit(f"找不到官方汉化数据：{p}\n请用 --source-patch 指定官方补丁的 patch 目录。")
    os.makedirs(args.out, exist_ok=True)

    # 基底：优先用本目录的模板（含 1.3.x 的额外正则逻辑），Map 位置留 __MAP__ 占位
    template_path = os.path.join(HERE, "zh-cn-patch.template.js")
    if os.path.isfile(template_path):
        src_js = open(template_path, encoding="utf-8").read()
        if "__MAP__" not in src_js:
            raise SystemExit(f"模板缺少 __MAP__ 占位标记：{template_path}")
        map_marker = "__MAP__"
    else:
        # 退路：直接用官方 JS，整体替换它的 Map 段
        src_js = open(src_js_path, encoding="utf-8").read()
        map_marker = None

    # ---- 还原官方界面翻译表（保持顺序）----
    # 表始终从「官方 JS」里读，模板只提供正文逻辑
    src_js_official = open(src_js_path, encoding="utf-8").read()
    orig_ui = {}
    start = src_js_official.index("new Map([")
    end = src_js_official.index("]);", start)
    for a, b in re.findall(r'"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"',
                           src_js_official[start + len("new Map(["):end], re.S):
        orig_ui[unescape_js(a)] = unescape_js(b)
    for a, b in re.findall(r"exact\.set\(\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*\)", src_js_official, re.S):
        orig_ui[unescape_js(a)] = unescape_js(b)

    # ---- 合并界面新增译文（覆盖旧词条）----
    ui_table = dict(orig_ui)
    overridden = [k for k in D.UI_NEW if k in ui_table]
    ui_table.update(D.UI_NEW)

    # ---- 官方文本翻译表 + 新增译文 ----
    trans = json.load(open(src_trans_path, encoding="utf-8"))
    entries = {e["hash"]: {"hash": e["hash"], "target": e["target"]} for e in trans["entries"]}
    added = 0
    for src, tgt in D.JSON_NEW.items():
        h = hashlib.sha256(src.encode("utf-8")).hexdigest()
        if h not in entries:
            added += 1
        entries[h] = {"hash": h, "target": tgt}

    pairs = ",\n    ".join(f"[{js_quote(k)},\n     {js_quote(v)}]" for k, v in ui_table.items())
    if map_marker:
        # 模板路线：只替换 __MAP__ 占位
        new_js = src_js.replace(map_marker, "[\n    " + pairs + "\n  ]", 1)
    else:
        # 退路：整体替换官方 JS 的 Map 段
        new_range = "new Map([\n    " + pairs + "\n  ]);"
        new_js = src_js[:start] + new_range + src_js[end + 2:]
    new_js = new_js.replace("/* eslint-disable */\n", "")

    with open(os.path.join(args.out, "zh-cn-patch.js"), "w", encoding="utf-8", newline="\n") as f:
        f.write(new_js)

    new_trans = {
        "patchVersion": args.patch_version,
        "gameVersion": args.game_version,
        "basedOn": "YeWu233/sudoku-mansion-zh-cn 1.2.7-zh-cn.1 (MIT)",
        "entries": sorted(entries.values(), key=lambda e: e["hash"]),
    }
    with open(os.path.join(args.out, "translations.json"), "w", encoding="utf-8") as f:
        json.dump(new_trans, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"界面翻译条目: {len(ui_table)}（官方 {len(orig_ui)} + 新增 {len(D.UI_NEW)}，覆盖 {len(overridden)}）")
    print(f"文本翻译条目: {len(entries)}（官方 {len(trans['entries'])} + 新增 {added}）")
    print(f"输出目录: {args.out}")


if __name__ == "__main__":
    main()

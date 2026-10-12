# Sudoku Mansion 简体中文汉化 · 1.3.2 适配版

[![game version](https://img.shields.io/badge/game-1.3.2-e8a83b)](https://store.steampowered.com/app/5005590/)
[![patch version](https://img.shields.io/badge/patch-1.3.2--zh--cn.1-e6c163)](#)
[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

《Sudoku Mansion（数独庄园）》的**非官方简体中文补丁**，适配游戏 **1.3.2**。

译文基础来自 [YeWu233/sudoku-mansion-zh-cn](https://github.com/YeWu233/sudoku-mansion-zh-cn)（官方汉化，支持到 1.2.7）。
本仓库在它之上完成 1.3.x 的适配与补译：**1.3.0 / 1.3.1 / 1.3.2 新增和改写的剧情、规则、提示、界面文本都已汉化。**

<img src="docs/screenshot-main-menu.png" alt="安装汉化后的中文主菜单：继续游戏 / 选项 / 制作人员 / 退出游戏" width="820">

<sub>安装后的主菜单（1.3.1 实机截图）：继续游戏 / 选项 / 制作人员 / 退出游戏 / 回到庄园。</sub>

> [English README](README.en.md)

## 汉化范围

| 项目 | 数量 |
| --- | --- |
| 文本翻译（剧情 / 房间 / 规则 / 帮助 / 目标） | 432 条（官方 384 + 新译 48） |
| 界面翻译（运行时 DOM 替换） | 608 条（官方 481 + 新译 127） |
| 安装时实际替换 | 每个文本文件 **439 处**，替换后**无残留英文** |

1.3.2 的内容全部覆盖：**三层金库分阶段 Boss**（三阶段：德国耳语 → 区域和 → 模线）、
改写后的笼子阶乘规则、新的扑克牌型规则、主厅 Mod / 楼梯间 Mod，以及新的首领关联界面文本。

## 下载与安装

1. 到 [Releases](../../releases) 下载 `Sudoku-Mansion-zh-CN-1.3.2-zh-cn.1.zip`（或用源码里的 `package/` 目录）。
2. 解压，**完全退出游戏**（任务管理器确认没有 `Sudoku Mansion.exe`）。
3. 在解压出的文件夹里打开 PowerShell：

   ```powershell
   python install.py
   ```

   也可以双击 `安装汉化-1.3.2.ps1`。

4. 从 Steam 正常启动游戏即可。

安装脚本会：自动定位 Steam 游戏目录 → 检查版本与文本匹配数量 → 备份 3 个原文件 →
写入译文并挂载汉化脚本。只想检查不改文件：`python install.py --dry-run`。
仅需 Python 3，安装/还原都不需要联网。

**还原英文**：`python restore.py`（或双击 `还原英文-1.3.2.ps1`）。
**安装自检**：`python verify.py`。

## 工作原理

- 文本翻译按**原文 SHA256 哈希**匹配：只替换完全匹配的英文串，
  所以换版本时不会误替换，匹配不到的内容保持英文而不会破坏游戏。
- 只修改 3 个数据文件（前端 `mansion.json`、后端 `mansion_default.json`、`index.html`），
  外加新增的 `zh-cn-patch.js` / `zh-cn-patch.css`。**不读写存档，不改游戏程序。**
- 界面部分的翻译由 `zh-cn-patch.js` 在页面加载时对 DOM 文本与
  `title / aria-label / placeholder / alt` 做精确匹配替换，并持续监听新增节点。
- 安装前会备份，失败自动回滚；`restore.py` 用备份还原，字节级一致。

## 更新日志

### 1.3.2-zh-cn.1 — 2026-10-12

- 适配游戏 **1.3.2**：新增 **16 条**文本译文、**16 条**界面译文，安装时替换 **439 处/文件**（原 428）。
  - **三层金库分阶段 Boss**（Phase 1/2/3）：相位制规则、阶段名称与三段解锁剧情
  - 改写后的**笼子阶乘**规则（笼内数字相乘 = N!）、新的**扑克牌型**规则
  - 新规则名：主厅 Mod、楼梯间 Mod
- **修复：检查错误数字弹窗整段是英文**
  - 原因：该弹窗正文由游戏拼成 `There are N wrong digits in this room.`，而原补丁的正则要求以句点结尾（`...wrong digits?\.$`），永远匹配不上。
  - 现在补齐了正文、`Remove wrong digits` / `Do nothing` / `Rewind` 三个按钮、回退说明（`Rewinding undoes the last N moves…`、撤销历史范围提示）以及 `All digits are correct!`。顺带补了弹窗常用词（关闭/确认/取消/确定…）。
- 工程改进：`zh-cn-patch.js` 的运行时逻辑改为由 `package/zh-cn-patch.template.js` 生成（`__MAP__` 占位），
  避免「重新生成词表时把手写正则逻辑冲掉」的旧问题；`install.py`/`restore.py`/`verify.py` 增加 BOM 容错。

### 1.3.1-zh-cn.1 — 2026-10-10

- 首个适配版：在官方 1.2.7 译文基础上适配 1.3.1，补译 1.3.0/1.3.1 的 32 段文本与 111 条界面字符串。

## Steam 又更新了怎么办

Steam 更新会覆盖 `index.html`（汉化入口丢失）和两个 `mansion.json`（译文还原为英文）。
因为按哈希匹配、不依赖固定版本号，所以**直接重跑 `python install.py` 就能恢复大部分汉化**，
新增文本会保持英文而不会报错。补译新增文本的流程：

```powershell
python package/merge_translation_data.py --game-root "<游戏目录>"   # 生成待补译清单
# 在清单里补好译文，再合并回数据并重新打包：
python package/merge_translation_data.py --apply-json <补好的 JSON>
python tools/build_package.py                                       # 重新生成 package/ 与 dist/
```

官方 1.2.7 的原始汉化数据放在 `.source/patch/`（不随仓库分发，需自行从上游项目获取），
`package/make_patch.py` 会把它与本仓库的新增译文合并成发布用数据
（正文逻辑取 `package/zh-cn-patch.template.js`，词表取官方 `translations.json` + `zh_cn_data.py`）。

## 已知限制

- 汉化依赖精确匹配，游戏改写过的界面词条会退回英文。
- 运行时界面翻译只覆盖表内字符串；游戏新加的界面文本需要补进 `zh_cn_data.py` 的 `UI_NEW`，
  由模板拼出来的动态文案（如计数类提示）需要在 `package/zh-cn-patch.template.js` 里加对应正则。
- 庄园编辑器（Mansion Editor）界面已完成大部分翻译，但个别术语未必与官方口径完全统一，欢迎反馈。

## 许可证与致谢

- 上游汉化：[YeWu233/sudoku-mansion-zh-cn](https://github.com/YeWu233/sudoku-mansion-zh-cn)（MIT）——
  本项目的绝大部分译文与注入思路来自该项目，详见 [THIRD-PARTY-NOTICES.md](package/THIRD-PARTY-NOTICES.md)。
- 本项目同样以 [MIT](package/LICENSE) 发布。
- 《Sudoku Mansion》由 Vault Door Studios 开发发行；本补丁**不包含**任何游戏本体文件、谜题数据或美术资源。

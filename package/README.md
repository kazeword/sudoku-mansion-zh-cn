# Sudoku Mansion 简体中文汉化 · 1.3.1 适配版

[![game version](https://img.shields.io/badge/game-1.3.1-e8a83b)](https://store.steampowered.com/app/5005590/)
[![patch version](https://img.shields.io/badge/patch-1.3.1--zh--cn.1-e6c163)](#)
[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

《Sudoku Mansion（数独庄园）》的**非官方简体中文补丁**，适配游戏 **1.3.1**。

译文基础来自 [YeWu233/sudoku-mansion-zh-cn](https://github.com/YeWu233/sudoku-mansion-zh-cn)（官方汉化，支持到 1.2.7）。
本仓库在它之上完成 1.3.x 的适配与补译：**游戏 1.3.0/1.3.1 新增和改写的剧情、规则、提示、界面文本都已汉化。**

> [English README](README.en.md)

## 汉化范围

| 项目 | 数量 |
| --- | --- |
| 文本翻译（剧情 / 房间 / 规则 / 帮助 / 目标） | 416 条（官方 384 + 新译 32） |
| 界面翻译（运行时 DOM 替换） | 592 条（官方 481 + 新译 111） |
| 安装时实际替换 | 每个文本文件 **428 处**，替换后**无残留英文** |

用 1.3.1 实测安装后的主菜单：继续游戏 / 选项 / 制作人员 / 退出游戏 / 回到庄园。

## 下载与安装

1. 到 [Releases](../../releases) 下载 `Sudoku-Mansion-zh-CN-1.3.1-zh-cn.1.zip`（或用源码里的 `package/` 目录）。
2. 解压，**完全退出游戏**（任务管理器确认没有 `Sudoku Mansion.exe`）。
3. 在解压出的文件夹里打开 PowerShell：

   ```powershell
   python install.py
   ```

   也可以双击 `安装汉化-1.3.1.ps1`。

4. 从 Steam 正常启动游戏即可。

安装脚本会：自动定位 Steam 游戏目录 → 检查版本与文本匹配数量 → 备份 3 个原文件 →
写入译文并挂载汉化脚本。只想检查不改文件：`python install.py --dry-run`。
仅需 Python 3，安装/还原都不需要联网。

**还原英文**：`python restore.py`（或双击 `还原英文-1.3.1.ps1`）。

## 工作原理

- 文本翻译按**原文 SHA256 哈希**匹配：只替换完全匹配的英文串，
  所以换版本时不会误替换，匹配不到的内容保持英文而不会破坏游戏。
- 只修改 3 个数据文件（前端 `mansion.json`、后端 `mansion_default.json`、`index.html`），
  外加新增的 `zh-cn-patch.js` / `zh-cn-patch.css`。**不读写存档，不改游戏程序。**
- 界面部分的翻译由 `zh-cn-patch.js` 在页面加载时对 DOM 文本与
  `title / aria-label / placeholder / alt` 做精确匹配替换，并持续监听新增节点。
- 安装前会备份，失败自动回滚；`restore.py` 用备份还原，字节级一致。

## 已知限制

- Steam 更新或"验证游戏文件完整性"会覆盖汉化：若游戏仍是 1.3.1，重跑 `install.py` 即可。
- 游戏升级到更高版本后，被改写的文本会保持英文（不会报错）。可按下面的流程补译。
- 汉化依赖精确匹配，游戏改写过的界面词条会退回英文。
- 庄园编辑器（Mansion Editor）的译名未必与官方术语完全统一，欢迎反馈。

## 游戏更新后怎么补译

```powershell
python tools/build_package.py            # 重新生成 package/ 与 dist/ 里的汉化数据
python package/merge_translation_data.py --game-root "<游戏目录>"   # 生成待补译清单
# 在清单里补好译文，再合并回数据并重新打包：
python package/merge_translation_data.py --apply-json <补好的 JSON>
python tools/build_package.py
```

官方 1.2.7 的原始汉化数据放在 `.source/patch/`（不随仓库分发，需自行从上游项目获取），
`make_patch.py` 会把它与本仓库的新增译文合并。

## 许可证与致谢

- 上游汉化：[YeWu233/sudoku-mansion-zh-cn](https://github.com/YeWu233/sudoku-mansion-zh-cn)（MIT）——
  本项目的绝大部分译文与注入思路来自该项目，详见 [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md)。
- 本项目同样以 [MIT](LICENSE) 发布。
- 《Sudoku Mansion》由 Vault Door Studios 开发发行；本补丁**不包含**任何游戏本体文件、谜题数据或美术资源。

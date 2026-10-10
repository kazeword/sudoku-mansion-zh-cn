# 第三方声明 / Third-Party Notices

## 上游汉化项目

本项目的绝大部分译文、运行时注入脚本（`zh-cn-patch.js` 的注入逻辑与模式匹配）以及安装思路，
来自 **YeWu233/sudoku-mansion-zh-cn**（《Sudoku Mansion》简体中文汉化补丁，适配游戏 1.2.7）：

- 仓库：https://github.com/YeWu233/sudoku-mansion-zh-cn
- 许可证：MIT License，Copyright (c) 2026 Sudoku Mansion Chinese Localization Contributors

本 1.3.1 适配版做的事情是：

1. 复用该项目的 384 条文本翻译表与 481 条界面翻译表；
2. 补译游戏 1.3.0 / 1.3.1 新增与改写的 32 段文本、111 条界面字符串；
3. 重新实现安装/还原脚本，使其按"原文 SHA256 哈希"匹配，不依赖固定的游戏文件哈希，
   因此在不同小版本之间也能安全安装（匹配不到就不替换，不会写坏游戏文件）。

上游 MIT 许可证的完整文本见本目录 `LICENSE`（版权声明已合并保留）。

## 游戏本体

《Sudoku Mansion》由 Vault Door Studios 开发发行。本补丁不包含任何游戏本体文件、
谜题数据或美术资源，安装时只在本机已购买的正版游戏文件上应用翻译。
游戏名称、原文文本及相关内容的权利归其各自权利人所有。

## 免责声明

本汉化是非官方玩家作品，与游戏开发者、发行商及 Steam 无关。使用前请先自行拥有正版游戏。

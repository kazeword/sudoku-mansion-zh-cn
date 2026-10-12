# Sudoku Mansion 简体中文汉化 · 1.3.2 适配版

[![game version](https://img.shields.io/badge/game-1.3.2-e8a83b)](https://store.steampowered.com/app/5005590/)
[![patch version](https://img.shields.io/badge/patch-1.3.2--zh--cn.1-e6c163)](#)
[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

《Sudoku Mansion（数独庄园）》的**非官方简体中文补丁**，适配游戏 **1.3.2**。

译文基础来自 [YeWu233/sudoku-mansion-zh-cn](https://github.com/YeWu233/sudoku-mansion-zh-cn)（官方汉化，支持到 1.2.7）。
本版在其之上完成 1.3.x 的适配与补译：**1.3.0 / 1.3.1 / 1.3.2 新增和改写的剧情、规则、提示、界面文本都已汉化。**

## 内容

| 项目 | 说明 |
| --- | --- |
| 适用游戏版本 | 1.3.2（Steam App ID 5005590，Windows） |
| 文本翻译 | 384 条（官方）+ 48 条新译 = 432 条 |
| 界面翻译 | 481 条（官方）+ 127 条新译 = 608 条 |
| 实际替换 | 每个文本文件 439 处，替换后无残留英文 |
| 依赖 | 仅需 Python 3；不联网、不读写存档 |

1.3.2 新增内容已全部覆盖，包括**三层金库分阶段 Boss**（三个阶段：德国耳语 → 区域和 → 模线）、
改写后的笼子阶乘规则与扑克牌型规则、主厅 Mod / 楼梯间 Mod 等。

## 安装

1. **完全退出游戏**（任务管理器里确认没有 `Sudoku Mansion.exe`）。
2. 在本文件夹打开 PowerShell：

   ```powershell
   python install.py
   ```

   或者直接双击 `安装汉化-1.3.2.ps1`。

3. 安装脚本会自动定位游戏目录（也可用 `--game-root "路径"` 指定），然后：
   - 检查游戏版本、统计可替换文本数量（1.3.2 正常为每个文件 439 处）；
   - 把要改的 3 个原文件备份到 `resources\zh-cn-backup-1.3.2-adapted-<时间戳>\`；
   - 写入译文、复制 `zh-cn-patch.js` / `zh-cn-patch.css`，并在 `index.html` 里挂载汉化脚本。

4. 从 Steam 正常启动游戏，界面即为中文。

只想检查、不改文件：

```powershell
python install.py --dry-run
```

## 还原英文

```powershell
python restore.py
```

从最近一次安装的备份还原 3 个原文件，并删除汉化脚本。（双击 `还原英文-1.3.2.ps1` 等同。）

## 安装结果自检

```powershell
python verify.py
```

检查：汉化文件是否就位、备份是否可用、两个文本文件能否正常解析且无残留英文、
`index.html` 入口是否注入正确。

## 原理与安全性

- 按**原文 SHA256 哈希**匹配译文：只替换完全匹配的字符串，游戏文本一变就不会误替换，
  匹配不到的内容保持英文而不会破坏游戏。
- 只动 3 个文件：`frontend\dist\browser\assets\mansion.json`、
  `backend\data\mansions\mansion_default.json`、`frontend\dist\browser\index.html`，
  另加两个新增的 `zh-cn-patch.js` / `zh-cn-patch.css`。
- **不读写存档**，不改游戏程序本身；安装失败自动回滚，还原后与安装前字节级一致。

## 版本修复说明（1.3.2-zh-cn.1）

- 适配游戏 1.3.2：三层金库分阶段 Boss、笼子阶乘规则、扑克牌型规则、主厅/楼梯间 Mod。
- **修复「检查错误数字」弹窗整段是英文**：该弹窗正文由游戏拼成
  `There are N wrong digits in this room.`，旧正则要求以句点结尾所以匹配不上；
  现在正文、`移除错误数字`/`不做处理`/`回退` 三个按钮、回退说明、`所有数字都正确！` 都已汉化。

## Steam 又更新了怎么办

Steam 更新会覆盖 `index.html`（汉化入口丢失）和两个 `mansion.json`（译文被还原成英文）。
本脚本按哈希匹配，不依赖固定版本号，所以：

- 如果新版本只是小改动 → 直接重跑 `python install.py`，已有译文照样生效，新增文本会保持英文。
- 想看新增了哪些文本 → 用 `tools/merge_translation_data.py --game-root "<游戏目录>"` 生成待补译清单，
  补好译文后用 `--apply-json` / `--apply-ui` 合并回数据，再重新运行 `make_patch.py`。

## 已知限制

- 运行时界面翻译依赖精确匹配，游戏改写过的界面词条会退回英文。
- 由游戏拼接出来的动态提示（计数类）需要正则支持，新增这类文案要改 `zh-cn-patch.template.js`。
- 庄园编辑器（Mansion Editor）界面已完成大部分翻译，个别术语未必与官方口径完全统一，欢迎反馈修正。

## 许可与致谢

- 上游：YeWu233/sudoku-mansion-zh-cn（MIT），译文与注入思路主要来自该项目，详见 `THIRD-PARTY-NOTICES.md`。
- 本适配版同样以 MIT 许可证发布，见 `LICENSE`。
- 《Sudoku Mansion》版权归 Vault Door Studios 所有；本补丁不含任何游戏本体文件。

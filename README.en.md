# Sudoku Mansion — Simplified Chinese Patch (adapted for 1.3.1)

[![game version](https://img.shields.io/badge/game-1.3.1-e8a83b)](https://store.steampowered.com/app/5005590/)
[![patch version](https://img.shields.io/badge/patch-1.3.1--zh--cn.1-e6c163)](#)
[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

An **unofficial Simplified Chinese localization** for *Sudoku Mansion*, adapted to game version **1.3.1**.

It builds on [YeWu233/sudoku-mansion-zh-cn](https://github.com/YeWu233/sudoku-mansion-zh-cn)
(the original community patch, which targets 1.2.7) and adds the text that 1.3.0 / 1.3.1
changed or introduced: new story beats, reworked puzzle rules, the new hint system, and new UI strings.

> [中文说明](README.md)

## Scope

| Item | Count |
| --- | --- |
| Story / room / rule / help / objective strings | 416 (384 upstream + 32 new) |
| Runtime UI strings (DOM replacement) | 592 (481 upstream + 111 new) |
| Replacements applied at install time | **428 per data file**, no English left behind |

## Install

1. Download `Sudoku-Mansion-zh-CN-1.3.1-zh-cn.1.zip` from [Releases](../../releases) (or use `package/`).
2. Extract it and **fully close the game** (make sure no `Sudoku Mansion.exe` is running).
3. In the extracted folder, run:

   ```powershell
   python install.py
   ```

   You can also double-click `安装汉化-1.3.1.ps1`.
4. Launch the game normally from Steam.

The installer locates the Steam install automatically, verifies the game version, counts the
matching strings, backs up the three original files, then writes the translation and hooks the
runtime script into `index.html`. Use `python install.py --dry-run` to check without touching
anything. Python 3 is the only requirement; no network access is needed.

**Restore English:** `python restore.py` (or double-click `还原英文-1.3.1.ps1`).

**Self-check:** `python verify.py`.

## How it works

- Text is matched by **SHA-256 of the original English string**, so a game update can never cause
  a wrong replacement — untranslated/changed strings simply stay English.
- Only three data files are modified (frontend `mansion.json`, backend `mansion_default.json`,
  `index.html`) plus the two added `zh-cn-patch.js` / `zh-cn-patch.css` assets.
  **Save files are never read or written**, and the game binary is untouched.
- UI strings are translated at runtime by exact-matching DOM text and
  `title / aria-label / placeholder / alt` attributes, with a MutationObserver for new nodes.
- Everything is backed up before writing; a failed install rolls back automatically, and
  `restore.py` restores the backup byte-for-byte.

## Known limitations

- Steam updates and "verify integrity of game files" overwrite the patch. Re-run `install.py`
  if the game is still 1.3.1.
- After a game update, reworded strings fall back to English (no errors, no breakage).
- The in-game Mansion Editor is translated too, but its wording may not match the official
  terminology everywhere — feedback is welcome.

## License & credits

- Upstream localization: [YeWu233/sudoku-mansion-zh-cn](https://github.com/YeWu233/sudoku-mansion-zh-cn) (MIT) —
  most of the translations and the injection approach come from that project.
  See [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).
- This adaptation is released under the [MIT license](LICENSE) as well.
- *Sudoku Mansion* is developed and published by Vault Door Studios. This patch contains **no**
  game files, puzzle data or art assets.

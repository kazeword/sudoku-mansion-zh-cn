# -*- coding: utf-8 -*-
"""Translated additions for Sudoku Mansion 1.3.1 (build on top of the 1.2.7 patch tables)."""

# 32 strings whose English text changed / was added in 1.3.0-1.3.1 (JSON game data)
JSON_NEW = {
"""You return to the fully revealed Main Hall as the Modular Conductor. Blue structures become coral rhythms across the same visible grid. \n\nMechanisms hidden beneath all three classes occupy one room without replacing one another. The mansion does not need to reveal more architecture. It changes how that architecture moves. \n\nPanels rotate beneath the marble. Chandeliers pulse in measured cycles. """:
"""你以模线指挥家的身份回到完全显现的主厅。蓝色结构在同一片可见盘面上化作珊瑚色的节奏。\n\n隐藏在三种身份之下的机关同处一室，却不再互相取代。庄园无需揭示更多建筑，它改变的是这些建筑的运转方式。\n\n大理石之下，面板缓缓旋转；枝形吊灯按着既定的周期明灭。""",

"""The final coral sequence settles. What the Conductor gains is a private route toward the Stairways. The assistant studies your appearance.\n\n"You look exactly like ..."\n\nHe catches himself.\n\n"... the Lord's child."\n\nThe way he says it carries admiration and something close to grief. """:
"""最后的珊瑚序列归于平静。指挥家得到的是通往楼梯间的私人通道。助手打量着你的模样。\n\n“你看起来简直就像……”\n\n他忽然停住。\n\n“……领主的那个孩子。”\n\n他说这话的语气里带着钦佩，也带着近乎悲痛的什么。""",

"""The staircase rises through dense fog. The German Whisperer's lines struggle to connect the clues. They disappear where the staircase expects larger structures. \n\nThe mansion is not preventing progress.  But this was never the route intended for a wandering guest.\n\nMaybe you need help from another class to progress here.""":
"""楼梯穿过浓雾向上延伸。德国耳语者的线路艰难地连接着线索，却在楼梯期待更大结构的地方中断。\n\n庄园并没有阻止你前进。只是这条路从来就不是为漫游的客人准备的。\n\n也许你需要另一个身份来帮你继续前进。""",

"""The Upper Foyer can be entered. Nothing inside can yet be solved. \nThe German Whisperer hears voices somewhere within the mist, but they offer no direction. \n\nYou are sure that this room will be solvable at some point. But not right now.""":
"""上层门厅已经可以进入，但里面还什么都解不开。\n德国耳语者听见雾中某处有人低语，却听不出方向。\n\n你确信这间房间总有一天能够解开，只是不是现在。""",

"""The Upper Foyer remains buried in fog. A few blue clues appear in front of the Ambassador. \n\nThey reveal nothing useful. No region can be completed. No path reaches far enough to matter.\n\nThe mansion has allowed an important visitor to stand at the threshold of its private world. No farther.\n\nMaybe someone else that is more accustomed to the inner workings of the mansion has to lead the way before you can follow.""":
"""上层门厅依然埋在雾中。使节面前浮现出几个蓝色的线索。\n\n它们揭示不了任何有用的东西。没有区域能够完成，没有路径能延伸得足够远。\n\n庄园允许一位重要的访客站到它私密世界的门槛前，但也仅止于此。\n\n也许得由更熟悉庄园内部运转的人先带路，你才能跟上。""",

"""You return to the Stairways as the Modular Conductor. The fog state remains exactly as it was left. Blue regions become coral rhythms. \n\nThe mansion remembers the Lord's child climbing these stairs. It remembers the pace, the hand against the railing. \n\n"It cannot be... You look exactly like them!," he repeats to himself.""":
"""你以模线指挥家的身份回到楼梯间。雾气仍保持原样，蓝色区域化作珊瑚色的节奏。\n\n庄园记得领主的那个孩子曾沿着这些楼梯向上走，记得那脚步的节奏，记得扶着栏杆的手。\n\n“不可能……你长得和他们一模一样！”他自言自语地重复着。""",

"""The final coral sequence settles. What changes now is permission. The private door at the top recognizes the Lord's child. The Upper Foyer opens fully for the first time. The assistant watches the doorway.\n\n"The Lord's child tried to stop the Lord."\n\nA pause.\n\n"I should have helped sooner.\"""":
"""最后的珊瑚序列归于平静。这一次改变的是许可。顶层的私门认出了领主的孩子，上层门厅第一次完全打开。助手注视着门口。\n\n“领主的孩子曾试图阻止领主。”\n\n一阵沉默。\n\n“我本该早些出手。”""",

"""The remaining coral mechanisms settle. \n\nNow revealed are fragments of the Lord's child's work:  Modular diagrams and repeated attempts to repair the system that the Lord broke.\n""":
"""其余的珊瑚机关也归于平静。\n\n此刻显现的是领主孩子工作的碎片：模线图纸，以及一次次试图修复领主所破坏的系统的尝试。\n""",

"""The Vault is different than any other room in the mansion. It is connected to rooms on each side.\n\nGreen paths enter from one direction. Blue regions from another. Coral mechanisms turn beneath both. """:
"""金库与庄园中任何其他房间都不同——它与两侧的房间相连。\n\n绿色路径从一侧进入，蓝色区域从另一侧进入，珊瑚色的机关在两者之下转动。""",

"""Deconstruction:\nFill the grid by drawing nine non-overlapping 3x3 square regions,\nsuch that each region contains the digits 1-9 once each and no digit repeats in any row or column.\n\nThe two digits in the overlap are part of such a 3x3 square region.\n\nCells outside these regions may contain digits from 1-9 in order to fulfill clues but are otherwise left blank. \n\nThese cells do not follow normal Sudoku rules and digits may be repeated, including with digits found within regions in the same row or column. \n\nFor the purpose of region sum lines, cells outside the regions may be partitioned into regions at any point between cells.""":
"""解构：\n在盘面上画出九个互不重叠的 3x3 正方形宫，\n使每个宫各包含一次 1-9，且任何一行、一列都不出现重复数字。\n\n重叠处的两个数字属于这样一个 3x3 宫。\n\n这些宫以外的格可以填入 1-9 的数字以完成线索，否则留空。\n\n这些格不遵循普通数独规则，数字可以重复，包括与同一行或同一列中宫内的数字重复。\n\n对于区域和线而言，宫以外的格可以在任意两格之间划分区域。""",

"""Coral light spirals across the dance floor. Your coat becomes a formal conductor's suit and the flute is replaced by a baton. \n\nYou have unlocked a new class: \n\n**The Modular Conductor** \n\nAcross the mansion, mechanisms respond. The Main Hall calls for you to make your way through the rooms to the Upper Foyer.\n\nThe assistant stares at your new appearance and all color leaves his face. But he says nothing.""":
"""珊瑚色的光在舞池上盘旋。你的外套变成正式的指挥礼服，长笛被指挥棒取代。\n\n你解锁了一个新身份：\n\n**模线指挥家**\n\n整个庄园的机关都开始回应。主厅召唤你穿过各个房间，前往上层门厅。\n\n助手盯着你的新模样，脸色瞬间煞白。但他什么也没说。""",

"""Hitpoint Arrows: A digit in a cell with an arrow is equal to the sum of all digits where the digit equals the distance from that arrow clue. \n\nIf multiple arrows are in one cell, the sum total of all such digits in those directions is used, but not all directions have to hit a valid digit.\n\nFor example, the cell directly next to an arrow is only counted by the arrow if it has a 1 in it. If any other digit is in that cell, it does not contribute to the sum total of the arrow cell. \n\nChoose "I need help" to see a graphical example for a valid 4x4 Hitpoint puzzle.""":
"""生命值箭头：箭头格中的数字，等于该箭头方向上所有“数字值恰好等于其与箭头距离”的数字之和。\n\n若同一格内有多个箭头，则将这些方向上所有此类数字相加；并非每个方向都必须命中有效数字。\n\n例如：紧邻箭头的格只有填入 1 时才会被该箭头计入；若为其他数字，则不计入箭头格的总和。\n\n点击“我需要帮助”可查看有效 4x4 生命值箭头谜题的图形示例。""",

"""For every cell in the puzzle: A cell in column X indicates the column where X appears in its row.\n\nFor example: The digits in column 1 show the positions of all 1s in the grid. Setting a 7 into R4C1 puts the 1 in this row into R4C7.\n\nChoose "I need help" to see a graphical example for a valid 4x4 Indexing puzzle.\n""":
"""谜题中的每一格：位于第 X 列的数字，表示该行中 X 出现的位置。\n\n例如：第 1 列中的数字显示出盘面上所有 1 的位置。在第 4 行第 1 列填入 7，就把这一行中的 1 放到第 4 行第 7 列。\n\n点击“我需要帮助”可查看有效 4x4 索引谜题的图形示例。\n""",

"""Cave logic:\nAll odd cells are orthogonally connected to each other.\n\nAll even cells are orthogonally connected through other even cells to the outside of the grid.\n\nDigits in gray circles are odd.\nDigits in gray squares are even.\n\nChoose "I need help" to see a graphical example for a valid Cave puzzle.""":
"""洞穴逻辑：\n所有奇数格在正交方向上彼此相连。\n\n所有偶数格通过其他偶数格在正交方向上与盘面外部相连。\n\n灰色圆圈中的数字为奇数。\n灰色方块中的数字为偶数。\n\n点击“我需要帮助”可查看有效洞穴谜题的图形示例。""",

"""If a digit is on a turquoise (dark stripes in colorblind mode) line, that many instances of that digit must be on that line.\n\nThe purple (vertical railway stripes in colorblind mode) line contains all 9 digits exactly once.""":
"""如果一个数字位于绿松石色（色盲模式下为深色条纹）线上，那么该数字在这条线上必须出现与自身数值相同的次数。\n\n紫色线（色盲模式下为竖直铁轨状条纹）上恰好包含全部 9 个数字各一次。""",

"""Spiral Galaxy: There is a single orthogonally connected region centered on the central cell of the grid that is symmetric under a 180° rotation. \n\nAll cells in the grid that contain odd digits belong to this galaxy, all even digits do not.\n\nDigits seperated by a X add to 10.\n\nChoose "I need help" to see a graphical example for a valid Galaxy puzzle.""":
"""螺旋星系：盘面中央格周围有一个单一的正交连通区域，该区域在 180° 旋转下是对称的。\n\n盘面中所有含奇数的格都属于这个星系，所有偶数格都不属于。\n\n被 X 分隔的数字之和为 10。\n\n点击“我需要帮助”可查看有效星系谜题的图形示例。""",

"""The three systems stop fighting. Green whispers. Blue regions. Coral rhythm. Each remains distinct. Together, they stabilize the Vault.\n\nA Master Key appears at the center, but with five empty positions orbiting its core. \nThe assistant stares at the unfinished key with disbelief.\n\n"This is the key to everything! But where are the remaining pieces?"\n\nHe sounds confused. """:
"""三种系统停止了争斗。绿色的低语、蓝色的区域、珊瑚色的节奏，各自保持独特。它们共同稳定了金库。\n\n一把总钥匙出现在中央，但核心周围还环绕着五个空位。\n助手难以置信地盯着这把未完成的钥匙。\n\n“这是通往一切的钥匙！可剩下的部分在哪里？”\n\n他的声音里满是困惑。""",

"""Spiral Galaxies: Divide the grid into galaxies, which are orthogonally connected groups of cells that have 180 degree rotational symmetry about their centers, and do not overlap with other galaxies. All cells must be part of a galaxy. The digits in each galaxy do not repeat and sum up to 27.\n\nAll circular clues (dots, quads, gray circles) are centers of galaxies. All centers of galaxies contain a circular clue.""":
"""螺旋星系：将盘面划分为若干个星系，星系是围绕中心具有 180 度旋转对称性的正交连通格组，且彼此不重叠。所有格都必须属于某个星系。每个星系中的数字不重复，且总和为 27。\n\n所有的圆形提示（点、四方格、灰色圆圈）都是星系的中心。所有星系的中心都包含一个圆形提示。""",

"""Inside the deeper Sanctuary, green, blue, and coral structures overlap completely. For the first time, you do not choose a class. You are all three. \n\nAt the center of it all stands the Lord. Beside him stands the assistant. Not imprisoned. Waiting. \n\nThe Lord speaks:\n\n"You solved my home."\n\nHis gaze passes over the rhythm of his child within you.""":
"""在更深处圣所的内部，绿色、蓝色和珊瑚色的结构完全重叠。你第一次无需选择身份——你同时是三者。\n\n这一切的中央站着领主。他身旁站着助手。不是被囚禁，而是在等待。\n\n领主开口了：\n\n“你解开了我的家。”\n\n他的目光扫过你体内属于他孩子的节奏。""",

"""At the front door, the assistant remains behind. Some servants have already refused his help. Others have given him work. He accepts both. \n\nFar beyond the house, the Lord remains before the silent portal. Whether it will ever answer him is no longer your decision. \n\nOutside, the earth is wet with morning mist. Your car stands where you left it. The invitation still lies on the passenger seat.\n\nThe final line has faded.\nOnly the first words remain: "Please come to Sudoku Mansion."\n\nYou drive away as sunlight reaches the garden. In the rear-view mirror, the house becomes smaller. \n\nFor one moment, three colors move through its windows. Green. Blue. Coral. Then they are gone.""":
"""在前门，助手留在了后面。有些仆人已经拒绝了他的帮助，另一些则给了他工作。他都接受。\n\n在房子之外很远的地方，领主仍停在沉默的传送门前。它是否还会回应他，已经不再由你决定。\n\n屋外，大地被晨雾打湿。你的车还停在你放下它的地方。邀请函仍躺在副驾驶座上。\n\n最后一行已经褪色。\n只剩下最初的字句：“请来数独庄园。”\n\n阳光照进花园时，你开车离开。后视镜里，房子越来越小。\n\n有那么一瞬间，三种颜色穿过它的窗户。绿色。蓝色。珊瑚色。然后它们消失了。""",

"""You will unlock a lot of additional rules on top of Normal Sudoku rules. \n\nClick on the rule on the left side or see the Rule Hints section in the menu to learn more about a newly unlocked rule.\n\nIt is normal that you will not be able to complete every grid the first time you see it.\n\nKeep exploring the mansion!""":
"""在标准数独规则之上，你还会解锁许多额外规则。\n\n点击左侧的规则，或在菜单中查看“规则提示”部分，了解新解锁的规则。\n\n第一次见到某个盘面时无法完成，是很正常的。\n\n继续探索庄园吧！""",

"""You will unlock a lot of additional rules on top of Normal Sudoku rules. \n\nPress {A} on a rule on the left side or see the Rule Hints section in the menu to learn more about a newly unlocked rule.\n\nIt is normal that you will not be able to complete every grid the first time you see it.\n\nKeep exploring the mansion!""":
"""在标准数独规则之上，你还会解锁许多额外规则。\n\n在左侧规则上按 {A}，或在菜单中查看“规则提示”部分，了解新解锁的规则。\n\n第一次见到某个盘面时无法完成，是很正常的。\n\n继续探索庄园吧！""",

"Puzzle Hints": "谜题提示",

"""If you ever feel stuck, there are specific hints for every puzzle in the Hint menu. \n\nEach hint is hidden until you are ready to need more help.\n\nIf you are still stuck, the link to the discord is in the main menu, where you can get more specific help.""":
"""如果你卡住了，提示菜单里为每个谜题都准备了专门的提示。\n\n每条提示在你真正需要帮助之前都是隐藏的。\n\n如果仍然卡住，主菜单中有 Discord 链接，可以在那里获得更具体的帮助。""",

"""There are multiple helpful controls in the lower right corner of the screen:\n\nIf you want to clean up pencil marks that are definitely wrong due to newly placed digits, press {L5} (Steam Deck only) to delete them.\n\nIf you ever feel stuck or think you made a mistake, you can always press {L4} (Steam Deck only) to see if there are mistakes in the grid.\n\nIf you want to completely restart a puzzle, press {R4} (Steam Deck only).\n\nAll of these are fully customizable and can be set as Actions on your personal Controller layout.\n\nYou can also turn on a dedicated Notes tab in the options to enter your own thoughts.""":
"""屏幕右下角有多种实用操作：\n\n若要清除因新填数字而确定错误的候选数，请按 {L5}（仅 Steam Deck）删除它们。\n\n若卡住或怀疑填错，可随时按 {L4}（仅 Steam Deck）检查盘面中的错误。\n\n若要彻底重开当前谜题，请按 {R4}（仅 Steam Deck）。\n\n这些都可以完全自定义，也可以设置为你个人手柄布局中的“动作”。\n\n你还可以在选项中开启独立的“笔记”标签，记录自己的想法。""",

"""If you ever want to reread the story of a room, on the right side you find the Lore and Epilogue tab.\nSelecting the tab again opens the text in a popup.""":
"""如果你想再次阅读某个房间的故事，可以在右侧找到背景故事和尾声标签。\n再次点击该标签会在弹窗中打开文本。""",

"""In the void, many things are suddenly allowed.\n\nBut lines will never overlap to occlude each other.\n\nIf lines are crossing each other or branching on cell corners, treat them as different lines.""":
"""在虚空中，许多事情突然变得允许了。\n\n但线条永远不会相互重叠遮挡。\n\n如果线条彼此交叉或在格角处分叉，请把它们视为不同的线。""",

"""You can draw lines with the controller.\n\nFor that, enter line mode by pressing {A} on the line symbol in the right column.\nSelect a color with the right stick.\n\nPressing {A} and releasing it cycles through O and X on this cell.\nSelect to adjacent cells before pressing {A} to create a X between the two cells.\nIf you move the left stick one cell before releasing {A} again, draw a line between the two cells.\nIf you hold {RB}/{LB} while doing that, you draw the edge line instead of the center line.\nBoth of these also work diagonally.\n\nTo create even longer lines, the functionality changes.\n\nPressing {A} and then tracing a path of at least 2 cells length draws the complete path through these cells, diagonal steps included.\n\nPressing {A} while holding {RB}/{LB} and selecting at least 3 cells draws the outer edge of the selected region.""":
"""你可以使用手柄绘制线条。\n\n先在右栏选中线条图标并按 {A}，进入线条模式；用右摇杆选择颜色。\n\n按下并松开 {A}，可在当前格循环放置 O 和 X。\n先选中相邻格，再按 {A}，可在两格之间放置 X。\n按住 {A}，将左摇杆移动一格后松开，即可在两格之间画线。\n进行上述操作时按住 {RB}/{LB}，会绘制边线而不是中心线。\n这些操作同样支持对角方向。\n\n若要绘制更长的线，功能会有所变化。\n\n按 {A} 后依次经过至少 2 格长度的路径，即可绘制穿过这些格的完整路径，包含对角步骤。\n\n按住 {RB}/{LB} 时按 {A} 并选中至少 3 格，会绘制所选区域的外边线。""",

"""Cells outside of the grid only contain digits to fulfill clues and else are left blank. \nDigits are always from the set 1-9 and can be repeated with any other digits in their row or column. There are no boxes.""":
"""盘面之外的格只填入为完成线索所需的数字，其余部分保持为空。\n盘面外的数字总是来自 1-9，并可与同一行或同一列中的其他数字重复。盘外没有宫。""",

"""Partition points divide region sum lines into equal sums. \n\nThe partition points are not given and may exist between any two cells. \n\nEvery region sum line must have at least one partition point.""":
"""分割点将区域和线分成相等的和。\n\n分割点不会给出，并且可能存在于任意两格之间。\n\n每条区域和线必须至少有一个分割点。""",

"""A digit in a cell with an arrow is equal to the sum of all digits where the digit equals the distance from that arrow clue. \nIf multiple arrows are in one cell, the sum total of all such digits in those directions is used.\n\nArrow Leap: Starting from each cell containing an arrow in the entire mansion, move in the direction of the arrow by a number of cells equal to the digit in that cell. If the destination lies outside the grid, the arrow's digit must be placed in that cell beyond the grid at that location. This is only possible in the mansion overview. """:
"""箭头格中的数字，等于所有“数字值恰好等于其与箭头提示距离”的数字之和。\n若同一格内有多个箭头，则将这些方向上所有此类数字相加。\n\n箭头跃迁：从整个庄园中每个含箭头的格出发，沿箭头方向移动与该格数字相等的格数。若目标位置在盘面之外，则必须把该箭头的数字填在盘面之外的那个格上。此操作只能在庄园总览中完成。""",

"Upper Foyer Mod": "上层门厅 Mod",
}

# UI (DOM) strings that were added or reworded in 1.3.0-1.3.1
UI_NEW = {
    # --- Hints / lore panels (chunk-LJ4SWAUZ.js) ---
    "Hidden hint, click to reveal": "隐藏的提示，点击查看",
    "Hint example": "示例提示",
    "No hints available yet.": "暂无可用提示。",
    "Select an entry from the list to read its hint.": "从列表中选择一项以阅读其提示。",
    "This room": "本房间",
    # --- Main shell / menus (main-QSONHEWG.js, chunk-SWOIZDDB.js) ---
    "I need help": "我需要帮助",
    "Mansion Editor": "庄园编辑器",
    "Move the selection": "移动选择",
    "Music volume": "音乐音量",
    "Mute music": "静音音乐",
    "Shift/Ctrl": "Shift/Ctrl",
    "Side column width": "侧栏宽度",
    "[sudoku-mansion] Import failed:": "[sudoku-mansion] 导入失败：",
    # --- Controller hints (chunk-RG23N7JF.js) ---
    "LB + A": "{LB} + {A}",
    "RB + A": "{RB} + {A}",
    # --- Editor UI (chunk-MID6GFPB.js) ---
    "(basic solving logic, shown in the Rule Hints menu)": "（基础解题逻辑，显示在“规则提示”菜单中）",
    "(color auto-detects via global Line Color Rules)": "（颜色通过全局线条颜色规则自动检测）",
    "(shown as the subtitle in the unlock notification)": "（显示在解锁通知的副标题中）",
    "(shown in class picker)": "（显示在身份选择器中）",
    "(shown in the reward picker + popup)": "（显示在奖励选择器和弹窗中）",
    "(shown in the unlocked rules panel)": "（显示在已解锁规则面板中）",
    "(≤10 chars, shown on button)": "（≤10 个字符，显示在按钮上）",
    "Achievement Config": "成就配置",
    "Add Class Variant": "添加身份变体",
    "Add Rule": "添加规则",
    "Add a rule in the Rules tab first.": "请先在“规则”标签中添加一条规则。",
    "All class variants are already placed at this position.": "所有身份变体都已放置在此位置。",
    "All devices": "所有设备",
    "Always visible": "始终可见",
    "Attach puzzle JSON": "附带谜题 JSON",
    "Auto-Detect Letters": "自动检测字母",
    "Auto-Detect Line Colors": "自动检测线条颜色",
    "Auto-detect": "自动检测",
    "Cannot move: solution conflict with existing room.": "无法移动：解答与现有房间冲突。",
    "Class Config": "身份配置",
    "Class group at (": "身份组位于 (",
    "Complete Objective": "完成目标",
    "Controller only": "仅手柄",
    "Delete Achievement": "删除成就",
    "Delete Class": "删除身份",
    "Delete Help Item": "删除帮助条目",
    "Delete Objective": "删除目标",
    "Delete Room": "删除房间",
    "Delete Rule": "删除规则",
    "Delete your save file? This cannot be undone.": "要删除你的存档吗？此操作无法撤销。",
    "Drag an image from the Images panel onto this area to override the default symbol.": "将图片面板中的图片拖到此处以替换默认符号。",
    "Drag an image from the Images panel onto this area.": "将图片面板中的图片拖到此处。",
    "Drop SudokuMaker JSON here": "将 SudokuMaker JSON 拖到此处",
    "Drop audio here": "将音频拖到此处",
    "Drop images here": "将图片拖到此处",
    'Each trigger fires its rewards when the configured cell is fog-revealed. Add a "Show Text Popup" reward for the popup text. Row and col are 1-indexed.':
        "每个触发器在指定格子的迷雾被清除时发放奖励。若要显示弹窗文本，请添加“显示文本弹窗”奖励。行号和列号从 1 开始。",
    "Element Visibility (": "元素可见性 (",
    "Failed to create mansion. Is the backend running?": "创建庄园失败。后端是否正在运行？",
    "Failed to delete mansion. Is the backend running?": "删除庄园失败。后端是否正在运行？",
    "Failed to delete save. Is the backend running?": "删除存档失败。后端是否正在运行？",
    "Failed to rename mansion. Is the backend running?": "重命名庄园失败。后端是否正在运行？",
    "Failed to save. Is the backend running?": "保存失败。后端是否正在运行？",
    "Failed to switch mansion. Is the backend running?": "切换庄园失败。后端是否正在运行？",
    "Failed to upload audio:": "上传音频失败：",
    "Failed to upload image:": "上传图片失败：",
    "Finish Game": "通关游戏",
    'Fires on entering the boss. Add a "Show Text Popup" reward for intro/story text.':
        "进入首领房间时触发。若要显示开场／剧情文本，请添加“显示文本弹窗”奖励。",
    'Fires on entering the room. Add a "Show Text Popup" reward for intro/story text.':
        "进入房间时触发。若要显示开场／剧情文本，请添加“显示文本弹窗”奖励。",
    "Go to Rules Tab": "前往“规则”标签",
    "Grant Achievement": "授予成就",
    "Grant Tutorial": "授予教程",
    "Help Item Config": "帮助条目配置",
    "Help Items": "帮助条目",
    "Hint Example Image": "示例提示图片",
    "Improve Rule": "强化规则",
    "Link to rooms, bosses, or popup triggers to complete automatically.": "关联房间、首领或弹窗触发器以自动完成。",
    "Mansion name:": "庄园名称：",
    "Mouse & keyboard only": "仅键鼠",
    "New Achievement": "新建成就",
    "New Class": "新建身份",
    "New Tutorial": "新建教程",
    "No free space found to ungroup this room.": "找不到可用空间来取消该房间的分组。",
    "Not placed": "未放置",
    "Not placed yet (": "尚未放置 (",
    "Objective Config": "目标配置",
    "Outside (hidden until unlocked)": "盘外（解锁前隐藏）",
    "Outside Room Type": "盘外房间类型",
    "Permanent (always visible)": "永久（始终可见）",
    "Pick a Rule": "选择规则",
    "Pick a built-in rule, or create a custom one.": "选择内置规则，或创建自定义规则。",
    "Pick a pictogram, or drag an image from the Images panel onto this room.": "选择图标，或将图片面板中的图片拖到该房间上。",
    "Popup Triggers (": "弹窗触发器 (",
    "Prototype room": "原型房间",
    "Re-import puzzle JSON": "重新导入谜题 JSON",
    "Remove Trigger": "移除触发器",
    "Renders above fog": "渲染在迷雾之上",
    "Reset to default": "重置为默认",
    "Rewards on Completion": "完成时的奖励",
    "Rewards on Defeat": "失败时的奖励",
    "Rewards on Entry": "进入时的奖励",
    "Room Config": "房间配置",
    "Room Types": "房间类型",
    "Rule Config": "规则配置",
    "Show Text Popup": "显示文本弹窗",
    "Shown on the Hints page between the rules and the hints.": "显示在提示页面中，位于规则与提示之间。",
    "Solving help for this variant": "此变体的解题帮助",
    "Theme Color": "主题颜色",
    "Tutorial Image": "教程图片",
    "Unlock Objective": "解锁目标",
    "Unlock Room Type": "解锁房间类型",
    "Unlock Rule": "解锁规则",
    "Upload tracks here, then pick the default music in the Mansion tab or override per room.":
        "在此上传曲目，然后在“庄园”标签中选择默认音乐，或为单个房间单独指定。",
    "Visible in this room only": "仅在此房间可见",
    "You have unsaved changes.": "你有未保存的更改。",
    "You have unsaved changes. Discard them and switch mansions?": "你有未保存的更改。要放弃更改并切换庄园吗？",
    "Create a placeholder boss without a puzzle": "创建一个没有谜题的首领占位符",
}

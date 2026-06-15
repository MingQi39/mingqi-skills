# 配图流水线（定稿标准 · 2026-06）

> **用户已确认当前 `assets/usable/` 出图效果为标准**。以后出稿 MUST 按本节执行，不要退回旧版（假 iOS 头、卡通图、小字贴边）。

完整流程见 `SKILL.md` Step 5。

---

## 定稿视觉规格（`tools/gen_memo_screenshots.py`）

| 项 | 值 | 说明 |
|----|-----|------|
| 画布 | **1242 × 1660** 竖版 | 小红书直传 |
| 背景 | `#EBEBEB` 灰 + 轻颗粒 | 不要状态栏/「备忘录」/「完成」 |
| 白卡片 | 圆角 16，上下左右各留 **56px** 灰边 | 只呈现正文区 |
| 文字左右留白 | 卡片内各 **120px** | 相对卡片内缘，非屏幕左缘 |
| 文字上留白 | 卡片顶下 **96px** 再起标题 | 小红书预览不顶头 |
| 标题下 | **无分隔线**，空 **32px** 接正文 | |
| 正文字号 | **38px 起**自动缩小至塞满（最低约 22px） | 苹方优先 |
| 标题字号 | 正文 +8，上限 **46px** | |
| 分块标题 | `【冬天主力】` 等，色 `#C45C26` | |
| 页脚日期 | **`FOOTER_DATE`** → 出图时填 **发布当天** `M.D`（如 `6.5`） | 用 `--date 2026-06-05` 指定；非日期页脚如 `还没签` 照写 |

**禁止再出现**：9:41、5G、备忘录、完成、标题下灰线、卡通茶杯封面、`gen_note_images.py`。

---

## 文案规范（`tools/memo_presets.py`）

**标题**：短、直白。例：`候鸟冬天去哪`、`医保异地备案`、`候鸟夏天再看`（分页用不同标题名，**不要 ①② 或 1 2**）。

**正文**：可多字、可换行；用【】分块；承接用「上条」「评论区」，**禁止 #19 等内部题号**。

**禁用词**：替我整理、我记的、干货、攻略、建议收藏。

**分页**：内容多就拆多张 PNG（如 #11 → `winter` + `summer`），每张独立标题，不用序号。

新题号：在 `memo_presets.py` 的 `NOTE_ASSETS` 增条目 → 跑脚本。

---

## 命令（出稿后 MUST 执行）

```bash
cd <skill 仓库根目录>
python3 tools/gen_note_assets.py --note <题号> --date YYYY-MM-DD
# 省略 --date 则用今天；多题可并列 --note
```

产出：**`assets/usable/*.png`**

可选从草稿 YAML 覆盖文案：

```bash
python3 tools/gen_note_assets.py --draft drafts/note11-候鸟冬天去哪.md
```

---

## 当前标准文件清单（可直接上传）

| 笔记 | 文件 | 上传顺序 |
|------|------|----------|
| #11 | `note11-memo-winter.png`、`note11-memo-summer.png` | 封面实拍 → 冬 → 夏 |
| #10 | `note10-memo-steps.png`、`note10-memo-check.png` | 封面实拍 → 步骤 → 确认项；**另补医保 App 实拍** |
| #1 | `note01-memo-sanya.png`、`note01-memo-walk.png` | 封面实拍 → 三城 → 步行 |
| #15 | `note15-memo-zufang.png` | 封面实拍 → 三个雷 |

---

## 封面（图 1，用户实拍，脚本不生成）

- 窗台/餐桌：茶杯 + 笔记本或地图，自然光，不露脸
- 多条笔记**复用同一张**，发布时在 App 加标题 ≤12 字
- 建议相册名：`养老-封面通用.jpg`

---

## 向用户交付（第 4 节）

1. PNG **路径** + **上传顺序**
2. 封面实拍一句说明
3. 实操帖标明须用户补 **官方 App 截屏**
4. 提醒用户**看图改字**（数字/政策）→ 改 `memo_presets.py` 再跑脚本

---

## 弃用

- `tools/gen_note_images.py`
- `tools/gen_cover.sh` / `gen_cover.sh.deprecated`
- `tools/gen_climate_table_handwritten.py`（除非用户明确要求纸纹大表）

---

## 依赖

Python 3 + Pillow；字体：PingFang / STHeiti（macOS）。

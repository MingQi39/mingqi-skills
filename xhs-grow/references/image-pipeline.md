# 配图流水线

> 出稿配图时 MUST 按本节执行。产出在 `assets/usable/`（本地，不入 git）。

完整流程见 `SKILL.md` Step 5。

---

## 视觉规格（`tools/gen_memo_screenshots.py`）

| 项 | 值 |
|---|---|
| 画布 | **1242 × 1660** 竖版 |
| 背景 | `#EBEBEB` 灰 + 轻颗粒 |
| 白卡片 | 圆角 16，四边各留 **56px** 灰边 |
| 文字左右留白 | 卡片内各 **120px** |
| 文字上留白 | 卡片顶下 **96px** 起标题 |
| 正文字号 | **38px** 起自动缩小（最低约 22px） |
| 分块标题 | `【小节名】`，色 `#C45C26` |
| 页脚日期 | `FOOTER_DATE` → 发布当天 `M.D` |

**禁止**：假 iOS 状态栏、卡通封面、营销海报风。

---

## 文案规范（`tools/memo_presets.py`）

- **标题**：短、直白，不要 ①② 序号
- **正文**：可多字；【】分块；禁止内部题号（如 #19）
- **禁用词**：替我整理、我记的、干货、攻略、建议收藏
- 新题号：在 `NOTE_ASSETS` 增条目后跑脚本

---

## 命令

```bash
python3 tools/gen_note_assets.py --note <编号> --date YYYY-MM-DD
python3 tools/gen_note_assets.py --draft drafts/note01-简称.md
```

产出：`assets/usable/*.png`

---

## 封面（图 1，用户实拍）

- 生活感场景：书桌、茶杯、窗外等，自然光，不露脸
- 多条笔记可复用同一张，App 内加标题 ≤12 字

---

## 向用户交付（输出第 4 节）

1. PNG 路径 + 上传顺序
2. 封面实拍说明
3. 实操帖标明须用户补 **官方 App 截屏**（打码）
4. 提醒看图改字 → 改 `memo_presets.py` 再跑脚本

---

## 依赖

Python 3 + Pillow；字体 PingFang / STHeiti（macOS）。

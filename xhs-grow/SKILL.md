---
name: xhs-grow
version: 2.0.0
description: "小红书养号与内容生产公共 skill。支持起号养号、热门选题检索、人味笔记写作、配图生成。用户先在 account-persona.md 配置账号人设；运营日志与草稿放 state/、drafts/（不入 git）。当用户提及「小红书」「养号」「写笔记」「该发什么」「下一条」「选题」「纯字」「文字笔记」「配图」「优化文案」时触发。"
---

# 小红书养号与内容生产 skill

## 触发场景

- 写小红书笔记 / 写下一条 / 该发什么了
- 养号 / 起号 / 账号定位
- 想选题 / 热门话题 / 什么选题火
- 纯字发 / 文字笔记 / 不要配图
- 出配图 / 优化文案 / 想标题

## 执行前必读（MUST）

任何笔记生产任务，**先按顺序读这 6 个文件**：

1. [`references/account-persona.md`](references/account-persona.md) — 账号人设（未填则先问用户）
2. [`references/humor.md`](references/humor.md) — 幽默基调（轻幽默 + 自嘲，克制）
3. [`examples/canonical-style.md`](examples/canonical-style.md) — 排版 / 标点 / 引述风格基准
4. [`references/algorithm.md`](references/algorithm.md) — 平台流量机制 + CES + 涨粉指标
5. [`references/anti-ai-checklist.md`](references/anti-ai-checklist.md) — 人味自检清单
6. [`references/sequel-strategy.md`](references/sequel-strategy.md) — 承接上条爆款时的铁律

**推荐选题 / 用户未指定具体题目时**，额外 MUST：

- [`references/hot-topics.md`](references/hot-topics.md) — 热门检索 SOP
- **WebSearch**（≥3 组检索词，见 hot-topics.md §二）

**纯字 / 文字笔记**时，额外读 [`references/publish-formats.md`](references/publish-formats.md)。

**配图模式**时，额外读 [`references/image-pipeline.md`](references/image-pipeline.md)。

## 本地运营数据（不入 git）

以下目录由用户在本地维护，**不要写入 git 仓库**：

| 路径 | 用途 |
|---|---|
| `state/` | 养号进度、数据追踪、热度快照（可选） |
| `drafts/` | 笔记草稿 |
| `assets/usable/` | 脚本生成的配图 PNG |

需要进度时问用户或读 `state/`（若存在），不要假设仓库里有日志。

## 内容生产流程

### Step 0：热门选题检索（先于写稿）

**触发**：「该发什么」「下一条」「想选题」、或未指定具体标题。

**MUST**：

1. 读 `hot-topics.md` + 用户提供的上条评论主题（若有）
2. **WebSearch** ≥3 组（赛道大盘 / 垂直 / 长尾）
3. 用 §三评分表给 2–3 个候选打分，只推荐 **总分 ≥14**
4. 输出时带 `热度依据: …` + 建议标题（≤13 字）+ 类型；等用户确认

**Sequel**：承接评论热门题时 MUST 读 `sequel-strategy.md`，用故事体包装，禁止复用爆款段落。

### Step 1：确认选题类型

| 类型 | 适用场景 | 模板 |
|---|---|---|
| **故事/避坑** | 第一人称叙事，涨粉主力 | [`templates/story.md`](templates/story.md) |
| **对比** | 多方案横向对比，收藏率高 | [`templates/compare.md`](templates/compare.md) |
| **实操** | 流程/清单；热题也须故事包装 | [`templates/tutorial.md`](templates/tutorial.md) |
| **吐槽/复盘** | 短帖，情绪化 | [`templates/rant.md`](templates/rant.md) |

### Step 2：核对真实信息（MUST）

- 政策 / 专业数据：**拒绝凭空生成**，让用户提供官方源
- 参考数据：文末「核对清单」列出待确认项
- 故事类：可编但要像真的（时间 / 地点 / 对话 / 细节）

### Step 3：按模板生产

读对应 `templates/<类型>.md`，严格按结构和约束生成。

### Step 4：人味自检

用 `anti-ai-checklist.md` 自查，**任何一条不过则重写**。

### Step 5：配图产出

用户明确 **纯字 / 文字笔记 / 不要配图** → 跳过，输出发布形态操作提醒。

否则（配图模式）：

1. 草稿写入本地 `drafts/note<编号>-<简称>.md`（可选 YAML `memo:` 块）
2. 在 `memo_presets.py` 配置题号后执行：`python3 tools/gen_note_assets.py --note <编号> --date YYYY-MM-DD`
3. 确认 `assets/usable/` 下 PNG 已生成
4. 封面优先用户实拍；暂无法拍可改发文字笔记

### Step 6：本地登记（可选）

若用户维护 `state/progress.md`，可 append 一条记录。**不自动 commit git**。

## 输出格式

### 选题推荐

1. **检索摘要**（2–4 条）
2. **推荐 1–3 个选题**（标题 ≤13 字 + 类型 + 总分 + 热度依据）
3. **不建议近期发的 1–2 个**（及原因）
4. **排期建议**（若用户在起号期）

### 笔记生产

1. **5 个标题备选**（全部 ≤13 汉字）
2. **正文**（400–600 字，纯文本，全角标点，禁止 Markdown）
2b. **加粗清单**（3–6 条原文字符串，供 App 内点 B）
3. **标签**（5–8 个）
4. **配图文件**或**发布形态**
5. **评论区互动话术**（3 条）
6. **核对清单**

## 红线（MUST NEVER）

- 不替任何产品 / 机构 / 中介背书
- 不出现「绝对」「稳赚」「包治」「一定」等绝对化用语
- 正文不出现微信号 / QQ / 手机号
- 不写「家人们」「姐妹们」「绝绝子」「干货满满」「建议收藏」
- 不用工整营销号结构（除非真在教流程）
- 无用户信源的政策 / 专业数据 **绝对不编**

## 排版与标点规范（MUST）

### 标点（全角）

| 用 | 不用 |
|---|---|
| `，` `。` `；` `：` `？` `！` `——` `……` | 半角 `,` `.` `;` `:` `?` `!` `--` `...` |

### 引号

引述别人说的话**直接写，不加引号**。仅短词 / 话术用直角引号「」。

### 数字 / 英文

中文与数字 / 英文之间加半角空格。

### 段落

- 段内不强行断行；每段 1–3 句；全文 5–8 段
- 段间空一行；无标号、无 bullet

### 重点加粗

- **§2 正文**：纯文本，无 `**`
- **§2b 加粗清单**：3–6 条，全文 3–6 处加粗

### 自检五步

1. 半角标点 → 改全角
2. 删 `**` `*`
3. 删多余引号
4. 数字 / 英文两侧空格
5. §2b 至少 1 条中段评论钩子

## 文件索引

| 路径 | 说明 |
|---|---|
| `references/account-persona.md` | 人设模板（用户填写） |
| `references/algorithm.md` | 流量机制 |
| `references/hot-topics.md` | 热门检索 SOP |
| `references/topic-pool-template.md` | 选题库模板 |
| `references/image-pipeline.md` | 配图标准与命令 |
| `tools/gen_note_assets.py` | 配图生成脚本 |
| `templates/` | 四类笔记模板 |
| `examples/` | 排版与好坏对照 |

# xhs-yanglao

小红书账号 **「我妈的养老地图」** 的全部运营资产 + 内容生产 skill。

> 36 岁独生女替我妈考察候鸟养老城市;异地养老 / 退休迁居 / 实操避坑。
> **叙事只写我妈,不出现我爸 / 父母 / 爸妈**(指代自家时)。
> 30 天起号计划已启动,SSOT 在 `state/progress.md`。

---

## 🚀 新电脑迁移(3 分钟搞定)

### 前置:确认依赖

本 skill 不依赖任何额外二进制(已弃用 `gen_cover.sh`,配图全部由用户手机拍 / 截图)。

macOS 自带的 git 即可。

### Step 1:克隆仓库到 skill 目录

```bash
mkdir -p ~/.agents/skills
git clone git@github.com:MingQi39/xhs-yanglao.git ~/.agents/skills/xhs-yanglao
```

(没配 SSH 就用 HTTPS:`git clone https://github.com/MingQi39/xhs-yanglao.git ~/.agents/skills/xhs-yanglao`)

### Step 2:验证 skill 加载

打开 AI(Claude / harness),直接问:

> 我现在做到哪了?

如果回答能说出「Day 0(2026-05-31)养号 ✅ + 资料 ✅,下一步 06-01 继续养号 30min」就装好了。

### Step 3:开干

完成 Step 1-2 后即可使用,**没有其他工具需要装**。配图自己拍,出稿走 AI。

---

## 📁 仓库结构

```
xhs-yanglao/
├── SKILL.md                    skill 入口(harness 自动加载)
├── README.md                   本文件
│
├── references/                 创作前必读(MUST)
│   ├── persona.md              账号人设 + 语气规则 + 红线
│   ├── algorithm.md            ⭐ 平台流量机制 + CES 公式 + 涨粉指标 + 8 条红线
│   ├── anti-ai-checklist.md    人味自检清单(发布前必过)
│   ├── publish-formats.md      配图 vs 文字笔记纯字(发布形态)
│   ├── topic-pool.md           30 个开播选题库(库存)
│   ├── hot-topics.md           ⭐ 热门检索 SOP + 热度排行
│   └── sources.md              政策/数据信源备查
│
├── templates/                  4 种笔记类型模板
│   ├── story.md                故事/避坑(涨粉主力)
│   ├── compare.md              多城市对比(收藏率高)
│   ├── tutorial.md             实操流程(粘性强)
│   └── rant.md                 吐槽/复盘(易爆款)
│
├── state/
│   └── progress.md             ⭐ Single source of truth(运营进度)
│
├── examples/
│   └── good-vs-bad-19.md       好/坏笔记对照
│
├── assets/                     选定的账号资产
│   ├── avatar.jpg              头像(窗台搪瓷茶杯+书)
│   └── banner.jpg              主页背景(木桌地图+茶杯+相机)
│
├── tools/                      (空,旧出图脚本已废弃,见 .deprecated)
└── .gitignore
```

---

## 📋 当前进度速览

详见 [`state/progress.md`](state/progress.md)。摘要:

- **当前阶段**:Phase 1 启动期(Day 0-3:养号 + 资料完善)
- **首发日期**:2026-06-03(Day 4)
- **首发笔记**:#19《我替我妈考察了 8 个城市,最后选了这个》(故事/避坑)
- **30 天计划**:5 阶段、16 条笔记

| 阶段 | 日期 | 目标 |
|---|---|---|
| Phase 1 启动 | 05-31 ~ 06-02 | 注册号、完善资料、养号 3 天 |
| Phase 2 立人设 | 06-03 ~ 06-09 | 首发 4 条,确立账号定位 |
| Phase 3 测内容 | 06-10 ~ 06-16 | 4 条,找数据最好的内容类型 |
| Phase 4 主攻爆款 | 06-17 ~ 06-23 | 4 条,主攻已验证的爆款类型 |
| Phase 5 沉淀变现 | 06-24 ~ 06-30 | 4 条 + 上架第一份资料 |

---

## 🎨 发布形态(配图 or 纯字)

曾经依赖 `tools/gen_cover.sh` 生成 AI 图;实测 AI 味不稳,**已停用**。

现在两种形态(详见 [`references/publish-formats.md`](references/publish-formats.md)):

| 形态 | 说明 |
|---|---|
| **配图模式**(默认) | 封面 + 内页用户自拍 / 截图;AI 只写「这张拍什么」,不给图 |
| **文字笔记模式**(可选) | App 内纯字 + 系统生成封面,**零额外出图**;适合首发测文案 |

不强制每条都拍照。冷启动 CTR 配图通常更好;允许用纯字探路,再用数据决定是否下条加 1 张生活感封面。

细节见 [`SKILL.md`](SKILL.md) 「Step 5:发布形态」。
---

## 🧠 创作流程(给 AI / 给你自己)

### 给 AI 用(自动激活)

直接对 AI 说以下任一,会自动加载本 skill:

- 「写一条养老笔记」「写下一条」「该发什么了」
- 「我做到哪了」「下一步是什么」
- 「想个标题」「出张封面」「优化文案」

### 给自己用(手动流程)

1. **读** [`references/persona.md`](references/persona.md) — 找回语气
2. **读** [`references/algorithm.md`](references/algorithm.md) — 想清楚怎么涨粉
3. **查热门** [`references/hot-topics.md`](references/hot-topics.md)(App 搜索 + 热度排行)
4. **挑选题** [`references/topic-pool.md`](references/topic-pool.md)(从热门优选里定 # 号)
5. **挑模板** `templates/<类型>.md`(故事 / 对比 / 实操 / 吐槽)
6. **写完过自检** [`references/anti-ai-checklist.md`](references/anti-ai-checklist.md)
7. **配图自理**(自己拍,见上一节)
8. **登记进度** append 一行到 `state/progress.md`

---

## 🔄 日常 git 流程

**AI 加载本 skill 后,每次改仓库内文件都会自动 commit + push**,无需你再手动提。

手动备份或自己改文件时,仍可用:

```bash
cd ~/.agents/skills/xhs-yanglao
git add -A
git commit -m "Day X: 描述"
git push
```

细则见 [`SKILL.md`](SKILL.md) 的「Git 自动同步」一节。

---

## 🚫 绝对红线(MUST NEVER)

详见 [`references/persona.md`](references/persona.md) + [`references/algorithm.md`](references/algorithm.md):

- 不替任何房产/养老社区/保险产品/中介背书
- 不出现「绝对/最/100%/包/治」等极限词
- 不诋毁任何城市
- 政策数据**必须**有用户给的官方源,**绝不**凭空生成
- 不写「家人们/姐妹们/绝绝子/今天给大家分享」等营销号腔
- AI 生成的图(如临时使用)发布时**必须**勾选「AI 辅助创作」;本账号默认配图全部由用户自拍,不应触发此项

---

## 📝 版本

- skill 版本:1.0.0
- 仓库:https://github.com/MingQi39/xhs-yanglao
- 创建日期:2026-05-31

---

## 🆘 常见问题

**Q:迁移后 AI 找不到 skill?**
A:确认目录是 `~/.agents/skills/xhs-yanglao/`(不是 `xhs-yanglao-export` 之类的子目录),且 `SKILL.md` 在根目录。

**Q:之前 README 里的 `gen_cover.sh` 还能用吗?**
A:已废弃。脚本被改名为 `tools/gen_cover.sh.deprecated` 留作纪念,新作不要再调它。配图自己拍。

**Q:`progress.md` 在两台电脑上分别改了,冲突了怎么办?**
A:迁移期间**只在一台机器上**改 progress。如果真冲突了,在新机器 `git pull` 时手动 merge——保留**两边的进度日志条目**(append-only),待办列表以**新机器为准**。

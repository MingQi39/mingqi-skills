# xhs-grow

小红书 **养号 + 内容生产** 公共 skill。适用于任意垂直赛道，用户自行配置人设与本地运营数据。

---

## 安装

```bash
# 从 mingqi-skills 安装
git clone git@github.com:MingQi39/mingqi-skills.git
cp -r mingqi-skills/xhs-grow ~/.agents/skills/xhs-grow

# 或仅克隆 skill 目录
mkdir -p ~/.agents/skills
ln -s /path/to/mingqi-skills/xhs-grow ~/.agents/skills/xhs-grow
```

或在 Cursor / Claude 中将本目录加入 skills 路径。

---

## 首次使用

1. 填写 [`references/account-persona.md`](references/account-persona.md)（账号昵称、赛道、叙述视角、叙事红线）
2. 可选：复制 [`references/topic-pool-template.md`](references/topic-pool-template.md) 到本地 `state/topic-pool.md`
3. 对 AI 说：「帮我写一条小红书笔记」或「该发什么了」

---

## 仓库结构

```
xhs-grow/
├── SKILL.md                    skill 入口
├── README.md
├── references/                 创作必读
│   ├── account-persona.md      人设模板（用户填写）
│   ├── algorithm.md            流量机制 + CES
│   ├── anti-ai-checklist.md    人味自检
│   ├── hot-topics.md           热门检索 SOP
│   ├── humor.md                幽默基调
│   ├── image-pipeline.md       配图标准
│   ├── publish-formats.md      纯字 vs 配图
│   ├── sequel-strategy.md      爆款承接策略
│   └── topic-pool-template.md  选题库模板
├── templates/                  故事 / 对比 / 实操 / 吐槽
├── examples/                   排版基准 + 好坏对照
├── tools/                      配图脚本
└── assets/                     头像封面等（可选）
```

**不入 git 的本地目录**（见 `.gitignore`）：

- `state/` — 进度、数据、热度快照
- `drafts/` — 笔记草稿
- `assets/usable/` — 生成的配图

---

## 创作流程（简版）

1. 读 `account-persona.md` 找回人设
2. 检索热门 → `hot-topics.md`
3. 选模板 → `templates/<类型>.md`
4. 写完过 `anti-ai-checklist.md`
5. 纯字或配图 → `publish-formats.md` / `image-pipeline.md`
6. 草稿与进度记在本地 `state/`、`drafts/`

---

## 配图命令

```bash
# 先在 tools/memo_presets.py 配置题号
python3 tools/gen_note_assets.py --note 1 --date 2026-06-25
```

产出：`assets/usable/*.png`（本地，不入库）

---

## 版本

- skill 版本：2.0.0
- 自 v2.0 起为公共养号 skill，不含个人运营日志

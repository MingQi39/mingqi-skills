# MingQi's Skills

个人 Cursor / Codex skill 集合。

## Skills

- **Project Learning Coach** (`project-learning-coach/`) — 项目驱动式代码库学习教练：架构摸底、追请求链路、每日任务、里程碑实战
- **Interview-Driven Learning** (`interview-driven-learning/`) — 视觉化面试驱动学习：先建知识地图，再按十阶段流程深度学习（定位 → 图谱 → 树 → 原理 → 机制 → 关联 → 项目 → 面试 → 压缩 → 回归图谱）

## Usage

安装到 Cursor：

```bash
cp -r project-learning-coach ~/.cursor/skills/
cp -r interview-driven-learning ~/.cursor/skills/
```

安装到 Codex：

```bash
cp -r project-learning-coach ~/.codex/skills/
cp -r interview-driven-learning ~/.codex/skills/
```

## 触发示例

**Project Learning Coach**

- 「学习这个项目 / 从哪开始」→ 模式 0 摸底
- 「今天学什么」→ 模式 1 每日任务
- 「追这条请求 / trace」→ 模式 2 追链路

**Interview-Driven Learning**

- 「面试准备 React Fiber」→ 从 ① 知识定位 + ② 知识图谱开始
- 「帮我压缩一下今天学的内容」→ ⑨ 压缩阶段
- 「这道面试题怎么答」→ ⑧ 面试阶段

建议在 Cursor **Settings → Rules → User Rules** 添加：

```markdown
当用户在学习代码库、理解项目架构、询问怎么学某个 repo、追请求链路、或布置每日学习任务时，必须先读取并遵循 project-learning-coach skill。

当用户进行面试准备、面试驱动学习、视觉化学习某个技术主题、或要求按知识图谱深度学习时，必须先读取并遵循 interview-driven-learning skill。
```

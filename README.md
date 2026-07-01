# MingQi's Skills

个人 Cursor / Codex skill 集合。

## Skills

- **Project Learning Coach** (`project-learning-coach/`) — 项目驱动式代码库学习教练：架构摸底、追请求链路、每日任务、里程碑实战

## Usage

安装到 Cursor：

```bash
cp -r project-learning-coach ~/.cursor/skills/
```

安装到 Codex：

```bash
cp -r project-learning-coach ~/.codex/skills/
```

## 触发示例

- 「学习这个项目 / 从哪开始」→ 模式 0 摸底
- 「今天学什么」→ 模式 1 每日任务
- 「追这条请求 / trace」→ 模式 2 追链路

建议在 Cursor **Settings → Rules → User Rules** 添加：

```markdown
当用户在学习代码库、理解项目架构、询问怎么学某个 repo、追请求链路、或布置每日学习任务时，必须先读取并遵循 project-learning-coach skill。
```

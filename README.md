# MingQi's Skills

Personal Cursor / Codex / OpenCode skill collection.

## Skills

- **Project Learning Coach** (`project-learning-coach/`) — Project-driven codebase learning: architecture survey, request tracing, daily tasks, milestone practice
- **AI Engineer Coach** (`ai-engineer-coach/`) — Learning OS for frontend -> AI application -> AI platform growth. Includes capability levels, knowledge tree updates, interview drill, and production readiness checks
- **KAN** (`kan/`) — Knowledge Atlas Navigator: spatial learning protocol. Atlas navigation, Zoom In/Out, Navigate, Knowledge Distance, interview-driven ten-stage flow

## Usage

Install to Cursor:

```bash
cp -r project-learning-coach ~/.cursor/skills/
cp -r ai-engineer-coach ~/.cursor/skills/
cp -r kan ~/.cursor/skills/
# Symlink (recommended)
ln -sfn "$(pwd)/kan" ~/.cursor/skills/kan
ln -sfn "$(pwd)/ai-engineer-coach" ~/.cursor/skills/ai-engineer-coach
```

Install to Codex:

```bash
cp -r project-learning-coach ~/.codex/skills/
cp -r ai-engineer-coach ~/.codex/skills/
cp -r kan ~/.codex/skills/
ln -sfn "$(pwd)/kan" ~/.codex/skills/kan
ln -sfn "$(pwd)/ai-engineer-coach" ~/.codex/skills/ai-engineer-coach
```

Install to OpenCode:

```bash
ln -sfn "$(pwd)/kan" ~/.config/opencode/skills/kan
ln -sfn "$(pwd)/ai-engineer-coach" ~/.config/opencode/skills/ai-engineer-coach
# ~/.config/opencode/AGENTS.md — global KAN rules
# ~/.config/opencode/opencode.jsonc — instructions + skill permissions
```

## Trigger examples

**Project Learning Coach**

- `learn this project / where to start` → mode 0 survey
- `trace this request` → mode 2 trace

**AI Engineer Coach**

- `design my 90-day AI engineer roadmap` → mode 0 system bootstrap
- `what should I do today to move to AI platform` → mode 1 daily execution
- `review this week and update my capability levels` → mode 4 weekly review
- `mock interview me from this project` → mode 5 interview drill

**KAN**

- `KAN: learn GIL` → Phase 0 atlas + ten stages
- `Zoom In Bytecode` → expand subtree
- `Navigate GIL → FastAPI` → path navigation
- `How are FastAPI and LangGraph related?` → Knowledge Distance
- `Mock interview asyncio` → interview tree

Optional Cursor **Settings → Rules → User Rules**:

```markdown
Codebase/repo learning → project-learning-coach.
Long-term AI career + capability tracking + interview prep → ai-engineer-coach.
Concepts / interviews / Zoom / Navigate → kan (~/.cursor/skills/kan/SKILL.md).
```

OpenCode uses `~/.config/opencode/AGENTS.md` + `kan` skill (no hook; load skill on learning prompts).

## KAN layout

```
kan/
├── SKILL.md          # Agent entry
├── SPEC/             # Specs (maintain these)
├── EXAMPLES/         # Reference output
└── README.md
```

Repo: [github.com/MingQi39/mingqi-skills](https://github.com/MingQi39/mingqi-skills)

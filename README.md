# MingQi's Skills

Personal Cursor / Codex / OpenCode skill collection.

## Skills

- **Project Learning Coach** (`project-learning-coach/`) — Project-driven codebase learning: architecture survey, request tracing, daily tasks, milestone practice
- **KAN** (`kan/`) — Knowledge Atlas Navigator: spatial learning protocol. Atlas navigation, Zoom In/Out, Navigate, Knowledge Distance, interview-driven ten-stage flow

> Former name `interview-driven-learning` merged into KAN v3.0.

## Usage

Install to Cursor:

```bash
cp -r project-learning-coach ~/.cursor/skills/
cp -r kan ~/.cursor/skills/
# Symlink (recommended)
ln -sfn "$(pwd)/kan" ~/.cursor/skills/kan
```

Install to Codex:

```bash
cp -r project-learning-coach ~/.codex/skills/
cp -r kan ~/.codex/skills/
ln -sfn "$(pwd)/kan" ~/.codex/skills/kan
```

Install to OpenCode:

```bash
ln -sfn "$(pwd)/kan" ~/.config/opencode/skills/kan
# ~/.config/opencode/AGENTS.md — global KAN rules
# ~/.config/opencode/opencode.jsonc — instructions + skill permissions
```

## Trigger examples

**Project Learning Coach**

- `learn this project / where to start` → mode 0 survey
- `trace this request` → mode 2 trace

**KAN**

- `KAN: learn GIL` → Phase 0 atlas + ten stages
- `Zoom In Bytecode` → expand subtree
- `Navigate GIL → FastAPI` → path navigation
- `How are FastAPI and LangGraph related?` → Knowledge Distance
- `Mock interview asyncio` → interview tree

Optional Cursor **Settings → Rules → User Rules**:

```markdown
Codebase/repo learning → project-learning-coach.
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

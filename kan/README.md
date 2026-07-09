# KAN — Knowledge Atlas Navigator

**Knowledge Atlas Navigator — Interview Driven Learning System**

> Don't teach me facts. Teach me how to navigate the map.

A spatial **Learning Protocol**, not a plain prompt. Maintain `SPEC/`; reference `EXAMPLES/`.

## Capabilities

| Capability | Description |
|------------|-------------|
| 📍 Knowledge Position | Where a concept sits in the field |
| 🗺️ Knowledge Atlas | Bird's-eye map (not a pure tree) |
| 🌲 Knowledge Tree | Single-node hierarchy |
| 🔍 Zoom In / Out | Map zoom |
| 🧭 Knowledge Navigation | Paths between concepts |
| 📏 Knowledge Distance | Hops between two concepts |
| ⚙️ First Principles | Ground truths |
| 💼 Real Project Link | Project mapping |
| 🎤 Interview | Interview tree + mock |
| 🧠 Compression | Navigation cards |
| 🔁 Review | Atlas state + review |

Install to Cursor:

```bash
cp -r kan ~/.cursor/skills/
ln -sfn "$(pwd)/kan" ~/.cursor/skills/kan
```

Install to Codex:

```bash
cp -r kan ~/.codex/skills/
ln -sfn "$(pwd)/kan" ~/.codex/skills/kan
```

Install to OpenCode:

```bash
ln -sfn "$(pwd)/kan" ~/.config/opencode/skills/kan
```

## Trigger examples

| You say | KAN does |
|---------|----------|
| `KAN: learn GIL` | Phase 0 atlas → ten-stage flow |
| `Zoom In Bytecode` | Expand Bytecode subtree |
| `Zoom Out` | Ascend bird's-eye |
| `Navigate GIL → FastAPI` | Path + step-by-step |
| `How are FastAPI and LangGraph related?` | Knowledge Distance |
| `Mock interview asyncio` | Interview tree + mock |
| `Compress today's learning` | Stage ⑨ navigation card |

## Layout

```
kan/
├── SKILL.md              # Agent entry
├── USER-RULE.md          # Cursor User Rules fallback
├── README.md             # This file
├── SPEC/
│   ├── 01-philosophy.md
│   ├── 02-learning-flow.md
│   ├── 03-atlas.md
│   ├── 04-navigation.md
│   ├── 05-interview.md
│   ├── 06-compression.md
│   └── 07-review.md
└── EXAMPLES/
    ├── GIL.md
    ├── navigation-samples.md
    └── engineer-atlas.md
```

## Roadmap

- **KAN v1.0** — Spec + SKILL entry (current)
- **KAN v2.0** — Persistent state, spaced review
- **KAN v3.0** — Agent auto-navigation, atlas auto-update

## vs project-learning-coach

- **Repo / trace requests** → `project-learning-coach`
- **Concepts / interviews / navigation** → `KAN`

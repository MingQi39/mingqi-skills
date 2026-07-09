# Review Specification

## Learning state (within session)

Record at end of each turn:

```text
Session Atlas State:
- Learned: [✓GIL, ✓Thread, ✓Coroutine]
- Current: [●asyncio]
- Next suggested: [FastAPI]
- Open branches: [Multiprocessing, Bytecode]
```

Cross-session: user says `continue last session` → restore Session Atlas State (or ask user to confirm if context is missing).

## Spaced review (lightweight)

User says `review` or `what should I review today`:

1. List compression cards for last 3–5 learned nodes
2. Ask one **navigation question** per node (`How many hops from X to Y?`) not definition drills
3. Wrong answer → Zoom In on the weak node

## Atlas auto-update

| Event | Action |
|-------|--------|
| Stage completed | Mark node on global map |
| ⑩ completed | Output updated global sub-map |
| User says `update atlas` | Merge all learned nodes |
| New topic starts | Attach to existing atlas; do not start an isolated island |

## Future extensions (v2+, optional now)

- Persist learned nodes to `state/atlas.json` (local user file, not in git)
- Auto-promote interview level (P5 mastered → suggest P6)
- Link with project-learning-coach: concepts from projects write back to KAN atlas

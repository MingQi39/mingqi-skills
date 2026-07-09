# Atlas Specification

## Phase 0 requirements

Before any teaching, draw the **complete knowledge atlas**. The atlas must answer:

| Question | Meaning |
|----------|---------|
| Where am I? | Current topic's place in the global map |
| What surrounds this topic? | Neighboring domains |
| Which concepts depend on it? | Downstream dependents |
| Which concepts does it depend on? | Upstream prerequisites |
| What concepts will I learn next? | What unlocks after this |

The atlas should feel like **Google Maps** — the user always knows where they are.

## Map vs tree (mandatory)

**Do not** use pure tree diagrams only. Use **multi-directional maps**.

### Good example

```text
                    Python
                        │
      ┌─────────────────┼────────────────┐
      │                 │                │
   Runtime         OOP            Concurrency
      │                               │
 Garbage Collection              GIL
      │                               │
  Memory Model             ┌─────┴─────┐
                           │           │
                        Thread      Process
                              │
                         asyncio
                              │
                         FastAPI
                              │
                         LangChain
                              │
                           Agent
```

### Bad example

```text
Python
├── Runtime
├── OOP
└── Concurrency
    └── GIL
```

Pure trees lack lateral links and cannot support navigation.

## ASCII drawing rules

1. **Nodes**: Concept names; standard casing (`asyncio`, `GIL`)
2. **Links**: `│` `─` `┌` `┐` `└` `┘` `┬` `┴` `┼`; vertical = layers, horizontal = sibling domains
3. **Current position**: Mark with `●` or `[●GIL]`
4. **Learned nodes**: Mark with `✓` or `(learned)`
5. **Width**: Max ~80 columns per diagram; split into regional sub-maps if wider
6. **Depth**: Bird's-eye 3–5 layers; details via Zoom In

## Atlas update rules

- After learning a node → **add it** to the global map; do not redraw unrelated regions
- ⑩ Back to the Atlas → redraw and highlight paths added/reinforced this session
- User says `update atlas` → merge all new nodes from the session

## Interview level tags (optional)

Annotate nodes to focus study:

- `P5` — fundamentals
- `P6` — mechanisms and engineering tradeoffs
- `P7` — architecture and production practice

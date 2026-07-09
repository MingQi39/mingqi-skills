# Navigation Specification

Core KAN capabilities: **Zoom** and **Navigate** like Google Maps.

## Zoom Out

**Trigger**: User says `Zoom Out` (optional layer count)

**Behavior**: Collapse upward along the parent chain; show a larger map.

**Example** — currently in GIL detail:

```text
Python
    ↓
Concurrency
    ↓
GIL
```

Further Zoom Out:

```text
Python Runtime
    ↓
Engineering Stack
```

**Rules**:
- Rise 1–2 layers per Zoom Out; do not jump to "everything" at once
- Keep current node marked `●`
- One sentence: what the user sees after zooming out

## Zoom In

**Trigger**: `Zoom In <node>` (e.g. `Zoom In GIL`, `Zoom In Bytecode`)

**Behavior**: Expand that node's sub-structure.

**Example** — `Zoom In GIL`:

```text
GIL
│
├── Why
├── How
├── Lock
├── Bytecode
├── CPU
├── IO
├── Multiprocessing
├── Coroutine
└── Production
```

**Example** — `Zoom In Bytecode`:

```text
Bytecode
    ↓
Compile
    ↓
VM
    ↓
Execution
    ↓
Switch Interval
    ↓
GIL
```

**Rules**:
- Aim for 5–12 child nodes
- Zoom In can recurse (user names a child)
- After Zoom In, ask: drill into which branch / Zoom Out / Navigate

## Navigate

**Trigger**: `Navigate <start> → <end>` or `Navigate <start> to <end>`

**Behavior**: Find a path on the atlas; **walk step by step** — no shortcut conclusion.

**Example** — `Navigate GIL → FastAPI`:

```text
GIL
    ↓
Thread
    ↓
Coroutine
    ↓
asyncio
    ↓
Event Loop
    ↓
FastAPI
    ↓
Request Handler
```

**Example** — `Navigate Coroutine → Agent`:

```text
Coroutine
    ↓
asyncio
    ↓
HTTPX
    ↓
LLM API
    ↓
LangChain
    ↓
ainvoke()
    ↓
Agent
```

**Rules**:
1. Draw the path first, then explain each hop (1–3 sentences per hop)
2. Label **why each hop connects** (mechanism or dependency)
3. If no path exists: state missing prerequisites; suggest what to learn first

## Knowledge Distance

**Trigger**: `How are A and B related?` / `Distance from A to B?`

**Behavior**:
1. **Do not** answer the relationship in prose first
2. Draw the path
3. State **Distance: N hops**
4. Walk hop by hop

**Example** — `FastAPI` and `LangGraph`:

```text
FastAPI
    ↓
HTTP
    ↓
asyncio
    ↓
Coroutine
    ↓
Task
    ↓
LLM
    ↓
LangChain
    ↓
LangGraph

Distance: 7 hops
```

Then explain each hop.

## Command cheat sheet

| User says | Agent does |
|-----------|------------|
| `Zoom Out` | Ascend bird's-eye |
| `Zoom In X` | Expand X's children |
| `Navigate A → B` | Draw path and walk through |
| `How are A and B related?` | Knowledge Distance |
| `Update atlas` | Merge session nodes into global map |
| `Where am I?` | Mark current node + surrounding neighborhood |

## Chinese command aliases (same behavior)

| Chinese | English equivalent |
|---------|-------------------|
| 放大 / Zoom In X | Zoom In X |
| 缩小 / Zoom Out | Zoom Out |
| 导航 A 到 B | Navigate A → B |
| A 和 B 什么关系 | Knowledge Distance |
| 我在哪 | Where am I? |
| 更新图谱 | Update atlas |
| 压缩 | Compress |
| 复习 | Review |
| 模拟面试 | Mock interview |
| 继续 | Continue (next stage) |

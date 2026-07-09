# GIL — Reference Example

> Demonstrates Phase 0 atlas + Zoom In + Navigate. Agent output should match this granularity.

## Phase 0 — Knowledge Atlas (excerpt)

```text
                    Python
                        │
      ┌─────────────────┼────────────────┐
      │                 │                │
   Runtime         OOP            Concurrency
      │                               │
 Garbage Collection              ●GIL
      │                               │
  Memory Model             ┌─────┴─────┐
                           │           │
                        Thread      Process
                              │
                         asyncio
```

## Zoom In GIL

```text
GIL
│
├── Why          # CPython refcount thread safety
├── How          # Global mutex
├── Lock         # Acquire/release timing
├── Bytecode     # Bytecode execution and switching
├── CPU          # CPU-bound: threads don't help
├── IO           # IO-bound: GIL impact is small
├── Multiprocessing
├── Coroutine    # Typical coroutine scenarios
└── Production   # Production tradeoffs
```

## Navigate GIL → FastAPI

```text
GIL → Thread → Coroutine → asyncio → Event Loop → FastAPI → Request Handler
Distance: 6 hops
```

## Compression Card

```text
┌─ GIL ─────────────────────────────────────┐
│ One-liner: CPython global mutex for refcount│
│ Position: Python → Concurrency → GIL       │
│ Depends: Thread, Memory Model              │
│ Unlocks: Multiprocessing vs asyncio choice │
│ Interview: "CPU or IO?" → IO impact smaller│
│ Navigate to: asyncio                       │
└────────────────────────────────────────────┘
```

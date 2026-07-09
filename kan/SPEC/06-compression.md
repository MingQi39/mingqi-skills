# Compression Specification

## Stage ⑨ Compression

Compress a learning session into a **portable navigation card**, not a bullet list of facts.

## Compression card format

```text
┌─ [Topic] ─────────────────────────┐
│ One-liner: [single-line position] │
│ Position: [path on global atlas]  │
│ Depends: [2-3 prerequisites]      │
│ Unlocks: [2-3 next nodes]         │
│ Mechanism: [3-5 step flow]        │
│ Interview: [top question + skeleton]│
│ Navigate to: [recommended next]   │
└───────────────────────────────────┘
```

## Decision tree (optional)

When the topic involves **choosing** an approach, add an ASCII decision tree:

```text
CPU-bound?
├── Yes → Multiprocessing
└── No → IO-bound?
         ├── Yes → asyncio / Coroutine
         └── No → Thread (watch GIL)
```

## Forbidden

- Pure definition bullets with no map position
- Facts without atlas location
- More than one screen (user must see where they are at a glance)

## Link to review

Compression card = review unit. User says `review GIL` → show card → offer Zoom In on weak branches.

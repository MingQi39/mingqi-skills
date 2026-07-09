# Engineer Atlas — Panorama

Reference map for Python → AI Platform Engineer. New nodes attach here.

```text
                 Python Runtime
                        │
        ┌───────────────┼──────────────┐
        │               │              │
     Memory         Concurrency     Networking
        │               │              │
       GC             GIL          HTTP/WebSocket
        │               │              │
        └──────┬────────┘              │
               │                       │
            asyncio ─────────────── FastAPI
               │                       │
               └──────────┬────────────┘
                          │
                     LangChain
                          │
                     LangGraph
                          │
                        Agent
```

## Usage

- Learn **any** new concept → mark insertion point on this map first
- After learning → add node; do not start an isolated atlas
- Interview prep → work backward from target role (AI Platform Engineer)

## User context (prefer when known)

- 6 years frontend: React / TypeScript / Zustand
- Target: AI Platform Engineer (not research scientist)
- Edge: interaction layer + engineering; learning Python / Agent / LangChain / LangGraph

Map Real Projects to user repos (e.g. `my-ai-studio`) when available.

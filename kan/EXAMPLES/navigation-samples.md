# Navigation Samples

## Zoom Out (ascend from GIL detail)

```text
Python
    ↓
Concurrency
    ↓
●GIL
```

## Zoom In Bytecode

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

## Knowledge Distance — FastAPI ↔ LangGraph

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

Explain in hop order; do not skip steps.

## Navigate Coroutine → Agent

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

## Cross-domain — Redis

```text
                    Storage
                        │
          ┌─────────────┼─────────────┐
          │             │             │
       Memory      Persistence    Networking
          │             │             │
       Eviction      RDB/AOF      Protocol
          │             │             │
       Cache ←──────── Cluster ──────→ Replication
          │
    AI Vector Cache
```

## Cross-domain — Transformer

```text
AI
    ↓
LLM
    ↓
Transformer
    ↓
Attention
    ↓
KV Cache
    ↓
RAG
    ↓
Agent
```

Same KAN protocol, any tech stack.

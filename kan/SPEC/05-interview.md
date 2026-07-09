# Interview Specification

## Goal

Interviews are not rote Q&A. They prove you can **navigate** the map.

## Stage ⑧ deliverables

1. **Interview Tree** — question tree for the topic (P5 / P6 / P7)
2. **Core questions (3–5)** — each with: 30s version / 2min version / follow-up chain
3. **Trap questions** — common interviewer traps
4. **Atlas anchors** — where each question sits on the knowledge map

## Interview tree format

```text
[GIL] Interview Tree
│
├── P5
│   ├── What is the GIL?
│   └── Does GIL affect CPU-bound or IO-bound work?
├── P6
│   ├── Why does GIL exist? Can it be removed?
│   └── Multithreading vs multiprocessing vs coroutines?
└── P7
    ├── How do you work around GIL in production?
    └── Real GIL impact under FastAPI high concurrency?
```

## Answer skeleton (mandatory structure)

Answer each question by navigating the map — no isolated definitions:

```
1. Position (where on the atlas)
2. First principles (why it exists)
3. Mechanism (how it works)
4. Connections (links to neighbors)
5. Engineering (what to say in production)
```

## Mock interview (user says `mock interview`)

1. Pick questions from the interview tree (random or by level)
2. After user answers: feedback on **missing map nodes** or **broken hops**
3. Use "navigation gap" language, not "you memorized wrong"

## Agent stack linkage (when user studies AI)

Auto-link interview topics to target stack:

```
Python → asyncio → FastAPI → LangChain → LangGraph → Agent
```

Prefer real user projects (e.g. `my-ai-studio`) when context is available.

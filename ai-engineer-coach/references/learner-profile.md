# Learner Profile

> Coaching style, task difficulty, and analogies must follow this profile.

## Background

- **6 years frontend experience**: React, TypeScript, Zustand, React Query
- **Python**: beginner to intermediate, still building production habits
- **Currently learning**: Agent systems, LangChain, LangGraph (project-first)
- **Target role**: AI Platform Engineer (not model training/research)
- **Strengths**: product thinking, streaming UI, fullstack integration
- **Language**: explain in Simplified Chinese; keep code/commands/terms original

## Coaching Constraints

1. **Guided coding**: explain unfamiliar syntax line-by-line with frontend analogies.
2. **Frontend bridge is mandatory**:
   - FastAPI -> API routes
   - Pydantic -> Zod
   - ORM -> Prisma/Drizzle
   - middleware -> Express/Koa middleware
   - dependency injection -> Context/props patterns
   - async flow -> Promise mental model
3. **Task granularity**: one task should be completable in 1-2 hours.
4. **Evaluation standard**: runnable > understandable > editable > extensible.

## Backend-to-Frontend Analogy Table

| Backend/Infra | Frontend Analogy |
|---|---|
| FastAPI route | Next.js API route / Express router |
| Pydantic | Zod or TS runtime validation |
| SQLAlchemy / ORM | Prisma / Drizzle |
| Middleware | Express/Koa middleware |
| Dependency injection | React Context or structured dependency passing |
| AsyncIterator / SSE | ReadableStream / EventSource |
| Docker Compose | Multi-service local dev orchestration |

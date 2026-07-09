---
name: ai-engineer-coach
description: >-
  Learning operating system for transitioning from frontend engineer to AI
  application engineer and AI platform engineer. Orchestrates project learning,
  capability growth, interview readiness, and long-term progress tracking.
---

# AI Engineer Learning OS

## Purpose

This skill is a **controller skill** that coordinates learning workflows across:

- Project understanding (`project-learning-coach`)
- Capability growth (platform-oriented competency tracking)
- Interview readiness (project-to-expression conversion)

Goal: avoid fragmented "repo reading" and build a durable progression:

`Frontend Engineer -> AI Application Engineer -> AI Platform Engineer`

## When To Use

Trigger when user asks for:

- Long-term AI learning roadmap
- How to learn multiple repos with cumulative growth
- Weekly/monthly progress planning
- "What did I gain" beyond "what did I read"
- Interview preparation based on project learning

## Controller Workflow (MUST)

1. Read learner profile and current progress state.
2. Determine current phase and select one mode.
3. Generate one executable study plan (1-2h task or one milestone).
4. Update:
   - knowledge tree
   - capability delta
   - progress log
5. Provide one interview expression or one mock question.

## Sub-skill Routing

### Primary routing

- Repository scanning / request tracing / daily repo task:
  - Route to `project-learning-coach`
- Capability leveling / career progression:
  - Route to platform competency logic in this skill (or `ai-platform-coach` if available)
- Interview simulation / scoring:
  - Route to interview mode in this skill (or `interview-coach` if available)

### Fallback if sub-skills are missing

If `ai-platform-coach` or `interview-coach` are not installed:

- Do not block.
- Use built-in templates under `references/` to perform equivalent behavior.
- Explicitly keep output sections:
  - Capability Delta
  - Knowledge Tree Update
  - Interview Check

## Modes

Detailed mode specs: `references/modes.md`

- **Mode 0 - System Bootstrapping**
  - Build baseline: current level, target level, first repo mission
- **Mode 1 - Daily Execution**
  - One concrete 1-2h task tied to capability ladder
- **Mode 2 - Repo-to-Capability Mapping**
  - Convert repository architecture into personal knowledge tree nodes
- **Mode 3 - Production Upgrade**
  - Add evaluation and observability checks to current understanding
- **Mode 4 - Weekly Review**
  - Consolidate growth, identify bottlenecks, set next-week target
- **Mode 5 - Interview Drill**
  - Mock Q&A with scoring and expression refinement

## Mandatory Output Contract

Each completed session must output:

1. `Today Mission`
2. `Capability Delta (LvX -> LvY)`
3. `Knowledge Tree Update`
4. `Production Readiness Check` (for AI projects)
5. `Interview Expression / Drill`
6. `Next Step`

## Production Readiness Requirement

For AI projects, always include:

- Evaluation search paths: `eval/`, `benchmark/`, tests, golden dataset
- Observability search paths: tracing, token usage, latency, error logs

If missing, assign one mini task to add or inspect one of them.

## Persistence and Fallback

Preferred write path:

- `{workspace}/.learning/progress.md`

If write access is unavailable:

- Return a copy-ready block beginning with:
  - `Please copy the following into .learning/progress.md`

Use `references/progress-template.md`.

## References

- `references/learner-profile.md`
- `references/competency-model.md`
- `references/knowledge-tree-template.md`
- `references/modes.md`
- `references/interview-mode.md`
- `references/progress-template.md`

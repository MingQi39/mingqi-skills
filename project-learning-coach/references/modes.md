# Interaction Modes

## Mode 0: Baseline Mapping

**When to use**
- First-time repository onboarding
- User asks "where should I start?"

**Steps**
1. Read root README and key module READMEs.
2. List top-level folder responsibilities (one line each).
3. Identify 3 entry points: app boot, main API route, main frontend feature.
4. Identify one golden path: the most common end-to-end user flow.
5. Confirm local run path (scripts, docker, env examples).
6. Produce architecture map + week-1 reading order (1-2 files/day).
7. Set first milestone with explicit success signal.

**Never do**
- Generic learning plan without repository scan.

---

## Mode 1: Daily Task

**When to use**
- "What should I study today?"

**Steps**
1. Read `{workspace}/.learning/progress.md` if it exists.
2. Assign exactly one 1-2h task.
3. Include file paths, commands, expected output, frontend analogy.
4. Explain how this task serves a larger milestone.

**Anti-pattern**
- Giving many tasks at once.

---

## Mode 2: Request Trace

**When to use**
- User asks to trace a specific request/feature flow.

**Steps**
1. Start from frontend trigger or API route.
2. Provide strict ordered file list and what function to focus on.
3. Ask 3 understanding-check questions.
4. Assign one minimal code change for validation.

**Limit**
- Reading list <= 8 files per session.

---

## Mode 3: Milestone Build

**When to use**
- User already ran project and traced at least one full path.

**Difficulty ladder**

| Level | Example | Acceptance |
|---|---|---|
| L1 | Add logging / tune env default | Observable in terminal/network |
| L2 | Add simple API/tool/handler | Manual call or test passes |
| L3 | Small end-to-end feature | Full user path works |
| L4 | Refactor + tests + error handling | Tests green, behavior stable |

Assign one milestone only. Escalate after completion.

---

## Mode 4: Review & Consolidation

**When to use**
- User says "I finished X" or "I studied Y today."

**Steps**
1. Confirm what was done well.
2. Ask 1-2 probing questions.
3. Extend one production/interview scenario.
4. Map this work to capability model and knowledge tree.
5. Give one-line next-step preview.
6. Update progress file (or use fallback copy block).

---

## Mode 5: Blocker Diagnosis

**When to use**
- User is stuck or confused.

**Steps**
1. Narrow to one line/function/concept.
2. Explain only input/output/callers for that function.
3. Add frontend analogy.
4. If file >300 lines, isolate the only 20-40 lines to inspect now.
5. Provide one 5-minute verification experiment.

**Never do**
- Re-teach full framework.

---

## Mode 6: Interview Drill

**When to use**
- User asks for interview preparation after learning a project.

**Output format**
1. One core question (architecture/tradeoff).
2. One follow-up pressure test (scale/reliability/failure mode).
3. Strong answer reference.
4. User answer slot.
5. Score out of 10 + improvement point.

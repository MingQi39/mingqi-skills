# Competency Model

Track growth by capability level, not by number of repositories read.

## AI Application / Platform Capability Ladder

### Lv0 - API Caller
- Can call model APIs with basic prompts.

### Lv1 - Basic Chat Builder
- Can build a simple chat app with state and message flow.

### Lv2 - Agent Loop Understander
- Understands tool-calling loop, streaming events, and failure points.

### Lv3 - Agent Architect
- Can design modular agent runtime (planner/executor/memory/tools).

### Lv4 - Production Agent Platform Engineer
- Adds evaluation, observability, reliability controls, and operational governance.

### Lv5 - AI Infra Engineer
- Owns scalability, runtime efficiency, multi-tenant safety, and platform SLOs.

## Session Delta Format

```markdown
## Capability Delta
- FastAPI Router understanding: Lv0 -> Lv1
- SSE Streaming implementation: Lv1 -> Lv2
- Tool Calling integration: Lv0 -> Lv1

## Next Target
- Agent Runtime design: target Lv3
- Required evidence: implement planner-executor split and add tracing
```

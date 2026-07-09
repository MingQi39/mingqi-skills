# AI Project Checklist

Use this checklist when the project includes LLM, agents, tool-calling, RAG, MCP, or streaming chat.

## Must-Find Files (priority order)

1. **Model integration layer**: adapters / clients / providers
2. **Chat entry path**: route + service
3. **Streaming protocol**: SSE/WebSocket event schema and formatting
4. **Tool system**: registry, handlers, tool schema transformation
5. **Agent loop**: ReAct/LangGraph/multi-step tool execution
6. **Frontend stream consumer**: EventSource/fetch-stream rendering by event type
7. **Evaluation layer**: `eval/`, `benchmark/`, test cases, golden datasets
8. **Observability layer**: tracing, token usage, latency, error logging

## Four Diagnostic Questions

1. What changes when switching from plain LLM reply to agent mode?
2. Who decides tool calls, and how are results fed back into context?
3. What stream event types exist, and how does UI handle each?
4. Which missing env keys make login work but break agent runtime?

## Recommended First Milestone

Add one minimal tool (for example `get_current_time`) and verify it is called through the real conversation/tool panel path.

## Production Readiness Reminder

A real AI system loop is:

`input -> agent -> output -> evaluation -> optimization`

Not just "prompt works once."

## Scope

- This checklist anchors **repository paths, implementation evidence, and AI production checks**.

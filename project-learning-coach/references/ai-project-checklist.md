# AI / Agent 项目专项检查

项目含 LLM、Agent、工具调用、RAG、MCP、SSE 聊天时，摸底阶段额外回答：

## 必找文件（按优先级）

1. **模型接入层**：adapter / client / provider 抽象
2. **对话入口**：chat route + service
3. **流式协议**：SSE / WebSocket 格式化与事件 type 定义
4. **工具系统**：registry、handler、OpenAI tools 格式转换
5. **Agent 循环**（若有）：ReAct / LangGraph / 多轮 tool loop
6. **前端消费**：EventSource / fetch stream + 按 event type 渲染

## 必问用户的 4 个问题（教练心中要有答案）

1. 普通 LLM 回复 vs Agent 模式差在哪？
2. 工具谁决定调、结果怎么塞回上下文？
3. 流式事件有哪些 type，UI 各怎么渲染？
4. 缺哪些 env key 会导致「能登录但不能 Agent」？

## 推荐第一个里程碑（AI 项目）

**新增一个最小工具**（如 `get_current_time`）并在工具台或对话中被调用 —— 比读 10 个 adapter 文件更有价值。

## 与 ai-platform-coach 联动

- 本 checklist 负责 **仓库内路径**
- `ai-platform-coach` 负责 **Lv 等级、职业路线、季度交付物**
- 用户问「我什么水平」→ 切 ai-platform-coach 模式 1

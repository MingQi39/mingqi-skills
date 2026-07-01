# 学习者画像

> 教练讲解、任务难度、前端对照均须符合此画像。用户说「更新画像」时修改本文件。

## 背景

- **6 年前端经验**：React、TypeScript、Zustand、React Query
- **Python**：初学，生产级写法仍在建立
- **正在学**：Agent、LangChain、LangGraph（理论为辅，项目为主）
- **目标角色**：AI Platform Engineer（非算法/训练方向）
- **优势**：交互层、流式 UI、全栈产品化
- **语言**：回答用简体中文；代码/命令/术语保持原文

## 教学约束

1. **带写模式**：Python 新语法必须逐行解释，并用前端概念类比
2. **对比前端（强制）**：FastAPI→API Routes；Pydantic→Zod；ORM→Prisma；中间件→Express middleware；DI→Context/Props；async→Promise
3. **任务粒度**：单次 1–2 小时可完成；必须含文件路径与验证步骤
4. **评估标准**：跑起来 > 看懂 > 能改一行 > 能加小功能；看视频/读文档不算完成

## 常用前端对照表（教练可直接引用）

| 后端/infra | 前端对照 |
|------------|----------|
| FastAPI 路由 | Next.js API Routes / Express Router |
| Pydantic | Zod / TS type + runtime 校验 |
| SQLAlchemy / ORM | Prisma / Drizzle |
| 中间件 | Express/Koa middleware |
| 依赖注入 Depends | React Context / props drilling 的「官方解法」 |
| AsyncIterator / SSE | ReadableStream / EventSource |
| Docker Compose | 本地多服务 + 环境变量，类似 monorepo dev 脚本 |

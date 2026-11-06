<div align="center">

<img src="assets/profile-header.svg" width="100%" alt="juzikuwei · AI 应用构建者 · 从想法到工作流，再到验证" />

**把 AI 产品想法，做成可测试、可观测、有证据支撑的工作流。**

简体中文 · [English](README.en.md) · [所有项目](https://github.com/juzikuwei?tab=repositories) · [联系我](mailto:juzidekuwei@outlook.com)

</div>

## 你好，我是 juzikuwei

我关注 **RAG、Agent 与评测**，喜欢把检索、工具调用和用户交互串成完整的应用。比起一次成功的输出，我更关心答案有没有依据、失败能不能定位、改动能不能验证。

我使用 Claude Code、Codex 和 Cursor 进行 AI 辅助开发：代码由 AI 编写，产品范围、架构取舍、审查与验收由我负责。

## 代表项目

### [AI / Agent Tech Radar](https://github.com/juzikuwei/tech-radar-agent)

**面向 AI 技术资料的研究助手，让回答可以追溯到检索证据。**

- 混合检索：结合语义检索与 BM25，使用 RRF 融合与 cross-encoder 重排。
- 有界 ReAct 工具调用、确定性引用校验，以及只读 MCP 服务。
- FastAPI + React 聊天界面，串起检索、回答与证据查看。

`Python` · `FastAPI` · `React` · `RAG` · `MCP`

[查看代码与使用说明 →](https://github.com/juzikuwei/tech-radar-agent#readme)

### [Focus Lab · 虚拟焦点小组](https://github.com/juzikuwei/focus-group-AI-Agent)

**从产品概念出发，生成虚拟受访者、多轮访谈与结构化洞察报告。**

- 串联受访者画像、主持提纲、访谈与报告，支持逐轮推进。
- 支持多种模型接口与可选的联网资料增强。
- 项目草稿和报告保存在浏览器本地，便于恢复与继续探索。

`JavaScript` · `Python` · `FastAPI` · `LangChain`

[查看代码与使用说明 →](https://github.com/juzikuwei/focus-group-AI-Agent#readme)

## 我怎样构建

| 环节 | 我关注的事 |
| --- | --- |
| 定义问题 | 先明确用户目标、范围和验收标准 |
| 设计工作流 | 让数据、证据、工具权限与失败路径清晰可见 |
| 与 AI 协作 | 用具体约束推进实现，审查关键改动与技术取舍 |
| 验证结果 | 用测试、评测与 Trace 检查行为，再迭代 |

**正在探索：** 会话上下文压缩、Agent 评测闭环、回答中每项结论的证据支持程度。

<details>
<summary>展开我的构建理念：地基、脚手架与可靠性</summary>

构建 Agent 系统像盖房子：工程原理是地基，框架是脚手架，具体的产品行为需要自己设计。

<img src="assets/mental-model-house-zh.svg" width="100%" alt="工程原理、框架和应用设计的房屋比喻" />

<img src="assets/mental-model-axes-zh.svg" width="100%" alt="构建能力与可靠性是需要共同提升的两个维度" />

先明确范围，再选择框架；先检查证据，再形成结论。把失败路径当作产品行为的一部分，用小实验验证大的设计决定。

</details>

<details>
<summary>展开贡献轨迹</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/juzikuwei/juzikuwei/output/github-contribution-grid-snake-dark.svg" />
  <img src="https://raw.githubusercontent.com/juzikuwei/juzikuwei/output/github-contribution-grid-snake.svg" width="100%" alt="GitHub 贡献记录蛇形动画" />
</picture>

</details>

---

欢迎交流 AI 应用、检索与 Agent 工程。**[juzidekuwei@outlook.com](mailto:juzidekuwei@outlook.com)** · 中文 / English · UTC+8

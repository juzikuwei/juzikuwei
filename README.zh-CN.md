<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:064e3b,100:0f766e&height=230&section=header&text=JUZIKUWEI&fontSize=54&fontColor=39d353&animation=twinkling&fontAlignY=36&desc=AI-native%20%E2%80%A2%20Vibe%20coding%20%E2%80%A2%20RAG%20%E2%80%A2%20Agents%20%E2%80%A2%20Evaluation&descAlignY=58&descSize=18" alt="Juzikuwei banner" />

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=22&duration=2600&pause=800&color=00E676&center=true&vCenter=true&width=820&lines=%24+whoami+%E2%86%92+AI-native+application+builder;%24+focus+%E2%86%92+RAG+%C2%B7+Agents+%C2%B7+Evaluation+%C2%B7+MCP;%24+how+%E2%86%92+AI+writes+the+code+%E2%80%94+I+architect+and+verify;%24+motto+%E2%86%92+grounded+answers+over+glossy+demos;%24+now+%E2%86%92+building+tech-radar-agent" alt="Typing introduction" />
</a>

<p>
  <img src="https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-00e676?style=for-the-badge" alt="当前语言：简体中文" />
  <a href="README.md"><img src="https://img.shields.io/badge/English-0d1117?style=for-the-badge" alt="Switch to English" /></a>
</p>

<p>
  <img src="https://komarev.com/ghpvc/?username=juzikuwei&style=for-the-badge&color=00e676&label=PROFILE+VIEWS" alt="Profile views" />
  <a href="mailto:juzidekuwei@outlook.com"><img src="https://img.shields.io/badge/Email-juzidekuwei%40outlook.com-064e3b?style=for-the-badge&logoColor=white" alt="Email" /></a>
  <a href="https://github.com/juzikuwei/tech-radar-agent"><img src="https://img.shields.io/badge/Featured-tech--radar--agent-0f766e?style=for-the-badge&logo=github&logoColor=white" alt="Featured project" /></a>
</p>

</div>

## 🖥️ ~/whoami

我构建 AI-native 应用，要求它们**可测试、可观测、有证据支撑**——是能在失败里活下来的工作流，而不是只在 demo 里好看的东西。

**我不手写代码——这里的每一行代码都由 AI（Claude Code 和 Codex）编写。** 架构设计、技术决策和验收测试由我负责。Vibe coding，按工程标准交付。

- 🔭 **正在做** — [AI/Agent Tech Radar](https://github.com/juzikuwei/tech-radar-agent)：混合检索（E5 + BM25 + RRF + cross-encoder）、有界 tool-calling ReAct agent、确定性引用校验、只读 MCP server
- 🧪 **在探索** — LangGraph、会话上下文压缩、agent 评测闭环、claim-level groundedness
- 🌏 **工作语言** — 中文 & English · UTC+8
- 📫 **联系我** — juzidekuwei@outlook.com

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0d1117,50:00e676,100:0d1117&height=3" alt="" />

## 🤖 ~/how-i-build

这里的每一行代码都由 AI 编写——与 Claude Code、Codex 和 Cursor 一起 vibe coding。分工如下：

| Mine | AI's |
| --- | --- |
| 架构、范围与 spec | 实现——全部代码 |
| 代码审查与设计质询 | 重构与样板代码 |
| 验收：测试、评测套件、Trace | 测试脚手架 |
| 决策记录与权衡取舍（ADR） | 文档草稿，由我编辑定稿 |

<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-0d1117?style=for-the-badge&logo=anthropic&logoColor=00e676" alt="Claude Code" />
  <img src="https://img.shields.io/badge/Codex-0d1117?style=for-the-badge&logo=openai&logoColor=00e676" alt="Codex" />
  <img src="https://img.shields.io/badge/Cursor-0d1117?style=for-the-badge&logo=cursor&logoColor=00e676" alt="Cursor" />
  <img src="https://img.shields.io/badge/Vibe%20Coding-059669?style=for-the-badge" alt="Vibe Coding" />
</p>

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0d1117,50:00e676,100:0d1117&height=3" alt="" />

## 🏗️ ~/mental-model

构建一个 agent 系统，就是在盖一栋房子：

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#0d1117','primaryTextColor':'#39d353','primaryBorderColor':'#00e676','lineColor':'#00e676','fontFamily':'monospace'}}}%%
flowchart LR
    A["📐 建筑工程原理<br/>承重 · 水电 · 防火规范<br/>━━━<br/>harness 问题清单：<br/>上下文 · 工具 · 状态 · 验证"]
    B["🏗️ 脚手架<br/>标准化钢结构<br/>━━━<br/>LangGraph：<br/>只解决编排，仅此而已"]
    C["🛋️ 装修与家具<br/>决定房子好不好住<br/>━━━<br/>你自己的代码：<br/>节点 · 压缩策略 · 工具设计"]
    A --> B --> C
```

脚手架从不决定房间住起来的感觉。框架解决的是编排；让 agent 值得信任的那些决策，没有现成脚手架。

两条轴线，一个系统：

- **构建** — 原理 × 编排 × AI 协作编码 → 决定它*能不能跑*
- **可靠** — 评测、生产反馈、业务正确性 → 决定它*能不能被信任*

只有轴一、没有轴二，交付的是 demo，不是系统。这里的代码由 AI 写——思考不是。

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0d1117,50:00e676,100:0d1117&height=3" alt="" />

## 🚀 ~/projects

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="https://github.com/juzikuwei/tech-radar-agent">
        <img src="https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=juzikuwei&repo=tech-radar-agent&hide_border=true&bg_color=00000000&title_color=00e676&icon_color=22d3ee&text_color=94a3b8" alt="AI/Agent Tech Radar" />
      </a>
      <p>
        <img src="https://img.shields.io/badge/Python-0d1117?style=flat-square&logo=python&logoColor=00e676" alt="Python" />
        <img src="https://img.shields.io/badge/FastAPI-0d1117?style=flat-square&logo=fastapi&logoColor=00e676" alt="FastAPI" />
        <img src="https://img.shields.io/badge/React-0d1117?style=flat-square&logo=react&logoColor=00e676" alt="React" />
        <img src="https://img.shields.io/badge/RAG-0d1117?style=flat-square&logoColor=00e676" alt="RAG" />
        <img src="https://img.shields.io/badge/MCP-0d1117?style=flat-square&logoColor=00e676" alt="MCP" />
      </p>
      <p><sub>Vibe-coded with Claude Code & Codex — human-owned architecture and acceptance.</sub></p>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="https://github.com/juzikuwei/focus-group-AI-Agent">
        <img src="https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=juzikuwei&repo=focus-group-AI-Agent&hide_border=true&bg_color=00000000&title_color=00e676&icon_color=22d3ee&text_color=94a3b8" alt="Focus Lab" />
      </a>
      <p>
        <img src="https://img.shields.io/badge/JavaScript-0d1117?style=flat-square&logo=javascript&logoColor=00e676" alt="JavaScript" />
        <img src="https://img.shields.io/badge/LangChain-0d1117?style=flat-square&logoColor=00e676" alt="LangChain" />
        <img src="https://img.shields.io/badge/Streaming-0d1117?style=flat-square&logoColor=00e676" alt="Streaming" />
        <img src="https://img.shields.io/badge/LLM_apps-0d1117?style=flat-square&logoColor=00e676" alt="LLM applications" />
      </p>
      <p><sub>Vibe-coded with Claude Code & Codex — human-owned architecture and acceptance.</sub></p>
    </td>
  </tr>
</table>

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0d1117,50:00e676,100:0d1117&height=3" alt="" />

## 🧭 ~/philosophy

```text
scope before framework
evidence before confidence
failure paths are product behavior
small experiments before large abstractions
ai writes, i verify
```

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0d1117,50:00e676,100:0d1117&height=3" alt="" />

## 📊 ~/stats

<div align="center">
  <img height="165" src="https://github-readme-stats-sigma-five.vercel.app/api?username=juzikuwei&show_icons=true&hide_border=true&rank_icon=github&bg_color=00000000&title_color=00e676&icon_color=22d3ee&text_color=94a3b8&ring_color=00e676" alt="GitHub statistics" />
  <img height="165" src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=juzikuwei&layout=compact&hide_border=true&bg_color=00000000&title_color=00e676&text_color=94a3b8&langs_count=6" alt="Top languages" />
</div>

<div align="center">
  <img src="https://streak-stats.demolab.com?user=juzikuwei&hide_border=true&background=00000000&ring=00e676&fire=22d3ee&currStreakLabel=22d3ee&sideLabels=4ade80" alt="GitHub contribution streak" />
</div>

<div align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=juzikuwei&theme=matrix&no-frame=true&no-bg=true&column=4&row=1&margin-w=6&margin-h=6" alt="GitHub trophies" />
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0d1117,50:00e676,100:0d1117&height=3" alt="" />

## 🎨 ~/contribution-art

<div align="center">

<img src="https://raw.githubusercontent.com/juzikuwei/juzikuwei/output/profile-night-green.svg" alt="3D contribution graph" width="100%" />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/juzikuwei/juzikuwei/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/juzikuwei/juzikuwei/output/github-contribution-grid-snake.svg" />
  <img alt="Contribution snake animation" src="https://raw.githubusercontent.com/juzikuwei/juzikuwei/output/github-contribution-grid-snake.svg" />
</picture>

</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0d1117,50:00e676,100:0d1117&height=3" alt="" />

## 🤝 ~/connect

我边做边分享真实过程：架构决策、别扭的边界情况、评测里的缺口，以及每一个让 AI 工作流更可信的小改进。

<p align="center">
  <a href="https://github.com/juzikuwei?tab=repositories"><img src="https://img.shields.io/badge/See_all_projects-059669?style=for-the-badge&logo=github&logoColor=white" alt="See all projects" /></a>
  <a href="mailto:juzidekuwei@outlook.com"><img src="https://img.shields.io/badge/Say_hello-juzidekuwei%40outlook.com-064e3b?style=for-the-badge&logoColor=white" alt="Email" /></a>
</p>

<div align="center">

<sub>公开地构建——一次一个可度量的工作流。</sub>

</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,50:064e3b,100:0d1117&height=140&section=footer&text=%3E%20EOF%20%E2%80%94%20thanks%20for%20visiting&fontSize=20&fontColor=39d353&fontAlignY=72" alt="" />

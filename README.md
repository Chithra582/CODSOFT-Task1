# CODSOFT Task 1 — Front-End Developer Portfolio 🌟

[![Spec: OpenGAP v0.1.0](https://img.shields.io/badge/spec-OpenGAP%20v0.1.0-blue)](https://github.com/open-gitagent/opengap)
[![Passport: Certified](https://img.shields.io/badge/HiDevs%20GitAgent%20Passport-Approved-purple)](https://app.hidevs.xyz/passport)
[![Category: Developer Tools](https://img.shields.io/badge/category-Developer%20tools-green)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> An interactive front-end developer portfolio and OpenGAP-compliant talent agent showcasing technical web design, CSS keyframe animations, React components, and responsive layouts by **Chithra R**.

---

## 🛡️ GitAgent Passport Checkpoint Compliance

| Checkpoint | Status | Details |
|---|---|---|
| **01. Validate** | ✅ **Passed** | Manifest in `agent.yaml` compliant with OpenGAP spec `0.1.0` in the **Developer tools** domain. |
| **02. Explain** | ✅ **Passed** | Complete `EXPLAINABILITY.md` covering decision logic, asset lineage, competency rubrics, and privacy boundaries. |
| **03. Export** | ✅ **Passed** | 4 Framework Visas earned (**OpenAI SDK**, **CrewAI**, **Claude Code**, and **Lyzr**). |

---

## 🗂️ Agent Repository Structure

```
CODSOFT-Task1/
├── agent.yaml              # OpenGAP manifest (v0.1.0)
├── SOUL.md                 # Agent persona, identity & developer craft values
├── RULES.md                # Hard constraints, responsive rules & privacy checks
├── DUTIES.md               # Segregation of duties policy & role boundaries
├── AGENTS.md               # Universal fallback agent instructions
├── EXPLAINABILITY.md       # Decision mechanics, data lineage & boundaries
├── index.html              # Clean portal entry with Passport badges
├── agent.py                # Validation runner, framework exporter & CLI
├── LICENSE                 # MIT License
│
├── CODSOFT Task1/          # Original Portfolio Source
│   ├── portfolio.html      # Interactive Portfolio Webpage
│   └── portfolio style.css # CSS Animations & Styles
│
├── images/                 # Image & Profile Assets
│
├── skills/                 # Capability modules
│   ├── portfolio-curation/
│   │   └── SKILL.md
│   ├── skills-assessment/
│   │   └── SKILL.md
│   └── project-showcase/
│       └── SKILL.md
│
├── tools/                  # MCP-compatible tool definitions
│   ├── get-developer-bio.yaml
│   ├── list-portfolio-projects.yaml
│   └── assess-skill-proficiency.yaml
│
└── adapters/               # Framework export targets for Passport Visas
    ├── openai_agent.py     # OpenAI Agents SDK export
    ├── crewai_agent.py     # CrewAI agent export
    ├── claude_code.json    # Claude Code configuration
    └── lyzr_agent.py       # Lyzr Studio adapter
```

---

## 🚀 Quick Start

### 1. View Portfolio
Open `index.html` or `CODSOFT Task1/portfolio.html` directly in any web browser.

### 2. Run OpenGAP Agent Validation
```bash
python agent.py --validate
```

### 3. Framework Exports (Visas)
```bash
python agent.py --export all
```

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).

# Tech Stack Docs

/**************************************************************
*         File: tech-stack.md
*         Author: A.Reid
*         Date: 1/8/2025
> [!info] Description \
> The Libraries, Packages and Technnologies \
> discovered, used, or abandoned in the     \
> process of developing **StellarAgent**    \
**************************************************************/

```ascii
    '########:'########::'######::'##::::'##::::'######::'########::::'###:::::'######::'##:::'##:
    ... ##..:: ##.....::'##... ##: ##:::: ##:::'##... ##:... ##..::::'## ##:::'##... ##: ##::'##::
    ::: ##:::: ##::::::: ##:::..:: ##:::: ##::: ##:::..::::: ##:::::'##:. ##:: ##:::..:: ##:'##:::
    ::: ##:::: ######::: ##::::::: #########:::. ######::::: ##::::'##:::. ##: ##::::::: #####::::
    ::: ##:::: ##...:::: ##::::::: ##.... ##::::..... ##:::: ##:::: #########: ##::::::: ##. ##:::
    ::: ##:::: ##::::::: ##::: ##: ##:::: ##:::'##::: ##:::: ##:::: ##.... ##: ##::: ##: ##:. ##::
    ::: ##:::: ########:. ######:: ##:::: ##:::. ######::::: ##:::: ##:::: ##:. ######:: ##::. ##:
    :::..:::::........:::......:::..:::::..:::::......::::::..:::::..:::::..:::......:::..::::..::
```

## Table of Contents
- [Tech Stack Docs](#tech-stack-docs)
	- [Table of Contents](#table-of-contents)
	- [✅ Project management](#-project-management)
		- [**Kanban Python**](#kanban-python)
			- [Description](#description)
		- [**Obsidian CLI**](#obsidian-cli)
			- [Description](#description-1)
	- [🛠️ Utilities](#️-utilities)
		- [**Typer**](#typer)
			- [Description](#description-2)
		- [**Rich**](#rich)
			- [Description](#description-3)
		- [**Textual**](#textual)
			- [Description](#description-4)
		- [**Dotenv Vault**](#dotenv-vault)
			- [Description](#description-5)
	- [📐 System Architecture](#-system-architecture)
		- [**IcePanel**](#icepanel)
			- [Description](#description-6)
		- [**D2**](#d2)
			- [Description](#description-7)
	- [📦 Containerization](#-containerization)
		- [**Docker**](#docker)
			- [Description](#description-8)
		- [**Hadolint**](#hadolint)
			- [Description](#description-9)
		- [**Lazy Docker**](#lazy-docker)
			- [Description](#description-10)
		- [**Slim**](#slim)
			- [Description](#description-11)
		- [**Dive**](#dive)
			- [Description](#description-12)
		- [**ctop**](#ctop)
			- [Description](#description-13)
		- [**Slick**](#slick)
			- [Description](#description-14)
	- [🌐 Networking](#-networking)
		- [**Caddy**](#caddy)
			- [Description](#description-15)
		- [**Nginx**](#nginx)
			- [Description](#description-16)
		- [**Tailscale**](#tailscale)
			- [Description](#description-17)
		- [**TSDProxy**](#tsdproxy)
			- [Description](#description-18)
	- [📡 Distributed Computing](#-distributed-computing)
		- [**Exo Explore**](#exo-explore)
			- [Description](#description-19)
	- [🧑🏾‍💻 Dev Env](#-dev-env)
		- [**PNPM**](#pnpm)
			- [Description](#description-20)
		- [**Turborepo**](#turborepo)
			- [Description](#description-21)
	- [🔗 Git](#-git)
		- [**Gitui**](#gitui)
			- [Description](#description-22)
		- [**czg**](#czg)
			- [Description](#description-23)
		- [**Left Hook**](#left-hook)
			- [Description](#description-24)
		- [**Lint-staged**](#lint-staged)
			- [Description](#description-25)
		- [❌ *Devmoji*](#-devmoji)
			- [Description](#description-26)
		- [❌ *Commitizen*](#-commitizen)
			- [Description](#description-27)
	- [🤖 QA Automation](#-qa-automation)
		- [**Ansible**](#ansible)
			- [Description](#description-28)
		- [**Codecov**](#codecov)
			- [Description](#description-29)
		- [**Renovate**](#renovate)
			- [Description](#description-30)
		- [**Sourcery**](#sourcery)
			- [Description](#description-31)
	- [🧪 Testing Frameworks](#-testing-frameworks)
		- [**Jest**](#jest)
			- [Description](#description-32)
	- [🪮 Linters \& Formatters](#-linters--formatters)
		- [**Markdownlint**](#markdownlint)
			- [Description](#description-33)
		- [**Biome**](#biome)
			- [Description](#description-34)
		- [**GPT Lint**](#gpt-lint)
			- [Description](#description-35)
		- [**MegaLinter**](#megalinter)
			- [Description](#description-36)
	- [🎮 AI Gateway \& Observability](#-ai-gateway--observability)
		- [**PortKey**](#portkey)
			- [Description](#description-37)
		- [**Not Diamond**](#not-diamond)
			- [Description](#description-38)
		- [**Open Router**](#open-router)
			- [Description](#description-39)
		- [**Opik**](#opik)
			- [Description](#description-40)
		- [**Posthog**](#posthog)
			- [Description](#description-41)
		- [**Trigger.dev**](#triggerdev)
			- [Description](#description-42)
	- [🛰️ Inference Providers](#️-inference-providers)
		- [**GLHF**](#glhf)
			- [Description](#description-43)
		- [**Gemini**](#gemini)
			- [Description](#description-44)
		- [**Mistral**](#mistral)
			- [Description](#description-45)
		- [**Cerebras**](#cerebras)
			- [Description](#description-46)
		- [**Sambanova**](#sambanova)
			- [Description](#description-47)
		- [**Groq**](#groq)
			- [Description](#description-48)
		- [**Together AI**](#together-ai)
			- [Description](#description-49)
		- [**HuggingFace Serverless Inference**](#huggingface-serverless-inference)
			- [Description](#description-50)
		- [**X AI**](#x-ai)
			- [Description](#description-51)
		- [**GitHub Models Inference**](#github-models-inference)
			- [Description](#description-52)
	- [⚡ Web Containers \& IDEs](#-web-containers--ides)
		- [**Codesandbox**](#codesandbox)
			- [Description](#description-53)
		- [**Stackblitz**](#stackblitz)
			- [Description](#description-54)
		- [**Lightning.ai**](#lightningai)
			- [Description](#description-55)
		- [**Project IDX**](#project-idx)
			- [Description](#description-56)
		- [**Windsurf**](#windsurf)
			- [Description](#description-57)
		- [**Bolt.diy**](#boltdiy)
			- [Description](#description-58)
		- [**Databutton**](#databutton)
			- [Description](#description-59)
		- [**Zed**](#zed)
			- [Description](#description-60)
	- [💡 IDE Coding Assistants](#-ide-coding-assistants)
		- [**Continue**](#continue)
			- [Description](#description-61)
		- [**Copilot Arena**](#copilot-arena)
			- [Description](#description-62)
		- [**Cline**](#cline)
			- [Description](#description-63)
	- [🦾 Internal Agents](#-internal-agents)
		- [**Browser Use \&\& LightRAG**](#browser-use--lightrag)
			- [Description](#description-64)
		- [**Open Interpreter**](#open-interpreter)
			- [Description](#description-65)
		- [**Fabric AI**](#fabric-ai)
			- [Description](#description-66)
		- [Pieces for Developers](#pieces-for-developers)
			- [Description](#description-67)
	- [💽 Database](#-database)
		- [**Couchbase**](#couchbase)
			- [Description](#description-68)
		- [**PostgreSQL**](#postgresql)
			- [Description](#description-69)
	- [☁️ Cloud](#️-cloud)
		- [**Google Cloud**](#google-cloud)
			- [Description](#description-70)
		- [**AWS**](#aws)
			- [Description](#description-71)
		- [**Oracle**](#oracle)
			- [Description](#description-72)
		- [**IBM**](#ibm)
			- [Description](#description-73)
	- [📸 Image \& Video Generation](#-image--video-generation)
		- [**Comfy UI**](#comfy-ui)
			- [Description](#description-74)



## ✅ Project management

### **Kanban Python**

#### Description

- Command-line interface for project management using Kanban methodology.
- [Kanban Python GitHub Repo](https://github.com/Zaloog/kanban-python)

### **Obsidian CLI**

#### Description

- Command-line interface for interacting with Obsidian knowledge base.
- [Docs](https://yakitrak.github.io/obsidian-cli-docs/)

==================================

## 🛠️ Utilities

---

### **Typer**

#### Description

- Fast, type-checked command-line interface generator for Python.
- [Docs](https://typer.tiangolo.com/)

### **Rich**

#### Description

- Python library for rich text and beautiful formatting in the terminal.
- [Docs](https://rich.readthedocs.io/en/latest/)

### **Textual**

#### Description

- Python library for rapidly building sophisticated TUIs

### **Dotenv Vault**

#### Description

- Secrets manager for .env files
==================================

## 📐 System Architecture

---

### **IcePanel**

#### Description

- Visual infrastructure design and documentation tool for modern software teams.
- [IcePanel Website](https://icepanel.io/)

### **D2**

#### Description

- Modern diagram scripting language that turns text to diagrams.
- [D2 Documentation](https://d2lang.com/)

==================================

## 📦 Containerization

---

### **Docker**

#### Description

- Platform for building, sharing, and running containerized applications.
- [Docker Docs](https://docs.docker.com/)
- [GenAI Series](https://www.docker.com/blog/tag/genai-docker-labs/)

### **Hadolint**

#### Description

- Dockerfile linter for maintaining best practices and preventing common mistakes.
- [GitHub](https://github.com/hadolint/hadolint)

### **Lazy Docker**

#### Description

- Terminal UI for Docker and Docker Compose with intuitive management features.
- [GitHub](https://github.com/jesseduffield/lazydocker?tab=readme-ov-file)

### **Slim**

#### Description

- Tool for analyzing and optimizing Docker container images.
- [GitHub](https://github.com/slimtoolkit/slim)

### **Dive**

#### Description

- Tool for exploring Docker image layers and reducing image size.
- [GitHub](https://github.com/wagoodman/dive)

### **ctop**

#### Description

- Top-like interface for container metrics monitoring.
- [GitHub](https://github.com/bcicen/ctop)

### **Slick**

#### Description

- Simplified container deployment tool using Caddy server.
- [GitHub](https://github.com/scmmishra/slick-deploy)

==================================

## 🌐 Networking

---

### **Caddy**

#### Description

- Fast, cross-platform HTTP/2 web server with automatic HTTPS.
- [Caddy Docs](https://caddyserver.com/docs)

### **Nginx**

#### Description

- High-performance web server and reverse proxy.
- [Nginx Docs](https://nginx.org/en/docs/)

### **Tailscale**

#### Description

- Secure, private network for connecting devices and services.
- [Tailscale Docs](https://tailscale.com/docs/)

### **TSDProxy**

#### Description

- TypeScript-based proxy server for development and testing.
- [GitHub](https://github.com/Mic92/tsproxy)

==================================

## 📡 Distributed Computing

---

### **Exo Explore**

#### Description

- Modern computing environment for developers and teams.
- [Website](https://exo.computer/)

==================================

## 🧑🏾‍💻 Dev Env

---

### **PNPM**

#### Description

- Fast, disk space efficient package manager for Node.js.
- [PNPM Docs](https://pnpm.io/installation)

### **Turborepo**

#### Description

- High-performance build system for JavaScript and TypeScript codebases.
- [Turborepo Docs](https://turbo.build/repo/docs)

==================================

## 🔗 Git

---

### **Gitui**

#### Description

- Git TUI
- [GitHub](https://github.com/extrawurst/gitui)

### **czg**

#### Description

- Commitizen for Git.
- [docs](https://cz-git.qbb.sh/)


### **Left Hook**

#### Description

- Fast and flexible Git hooks manager.
- [Docs](https://evilmartians.github.io/lefthook/)
- [GitHub](https://github.com/evilmartians/lefthook)

### **Lint-staged**

#### Description

- Run linters on git staged files to ensure code quality.
- [GitHub](https://github.com/okonet/lint-staged)

### ❌ *Devmoji*

- (removed)

#### Description

- Emoji tool for conventional commits and git messages.
- [GitHub Repo](https://github.com/folke/devmoji)

### ❌ *Commitizen*

- (removed)

#### Description

- Tool for creating standardized commit messages.
- [GitHub Repo](https://github.com/commitizen/cz-cli)

==================================

## 🤖 QA Automation

---

### **Ansible**

#### Description

- Automation tool for configuration management and application deployment.
- [Docs](https://docs.ansible.com/ansible/latest/index.html#)

### **Codecov**

#### Description

- Code coverage reporting and monitoring tool.
- [GitHub Repo](https://github.com/codecov/codecov-action)
- [Docs](https://docs.codecov.com/docs/quick-start)

### **Renovate**

#### Description

- Automated dependency updates across multiple platforms and languages.
- [GitHub](https://docs.renovatebot.com/)

### **Sourcery**

#### Description

- Automated Code Review and Coding Assistants.
- [Docs](https://docs.sourcery.ai/Sourcery/)



==================================

## 🧪 Testing Frameworks

---

### **Jest**

#### Description

- Delightful JavaScript testing framework with a focus on simplicity.
- [Docs](https://jestjs.io/docs/getting-started)

## 🪮 Linters & Formatters

---

### **Markdownlint**

#### Description

- Style checker and linter for Markdown files.

### **Biome**

#### Description

- Fast formatter, linter, and bundler for JavaScript, TypeScript and more.

### **GPT Lint**

#### Description

- AI-powered code linting tool.

### **MegaLinter**

#### Description

- Tool for detecting and fixing technical debt.

==================================

## 🎮 AI Gateway & Observability

---

### **PortKey**

#### Description

- API Gateway and management platform for AI models.
- [Docs](https://portkey.ai/docs/introduction/what-is-portkey)

### **Not Diamond**

#### Description

- AI platform for secure and efficient model deployment.
- [Docs](https://notdiamond.ai/)

### **Open Router**

#### Description

- Unified API gateway for multiple AI models and providers.
- [Docs](https://openrouter.ai/docs)

### **Opik**

#### Description

### **Posthog**

#### Description

- Open-source product analytics platform.
- [Docs](https://posthog.com/)

### **Trigger.dev**

#### Description

- Trigger.dev v3 makes it easy to write reliable long-running tasks without timeouts.


- [Docs](https://trigger.dev/docs/introduction)
==================================

## 🛰️ Inference Providers

---

### **GLHF**

#### Description

- AI platform for game development and interaction.
- [API Settings](https://glhf.chat/users/settings/api)

### **Gemini**

#### Description

- Google's multimodal AI model with advanced reasoning capabilities.
- [Gemini API](https://ai.google.dev/gemini-api/docs)

### **Mistral**

#### Description

- Powerful large language model with state-of-the-art performance.
- [Mistral API](https://docs.mistral.ai/)

### **Cerebras**

#### Description

- AI compute platform for large-scale model training and inference.
- [Docs](https://inference-docs.cerebras.ai/introduction)

### **Sambanova**

#### Description

- AI accelerator platform for enterprise deployments.
- [Sambanova Cloud](https://cloud.sambanova.ai/apis)

### **Groq**

#### Description

- High-performance AI inference platform.
- [Groq Cloud](https://groq.com/)

### **Together AI**

#### Description

- Platform for deploying and scaling AI models collaboratively.
- [Together AI Docs](https://docs.together.ai/)

### **HuggingFace Serverless Inference**

#### Description

- Serverless solution for deploying machine learning models.
- [Docs](https://huggingface.co/docs/inference-endpoints/index)

### **X AI**

#### Description

- Advanced AI models and tools from X (formerly Twitter).
- [Docs](https://platform.openai.com/docs/guides/gpt)

### **GitHub Models Inference**

#### Description

- GitHub's AI-powered code generation and analysis tools.
- [Docs](https://github.blog/2023-11-08-universe-2023-github-copilot-transforms-into-an-ai-powered-developer-experience/)

==================================

## ⚡ Web Containers & IDEs

### **Codesandbox**

#### Description

- Online IDE for rapid web development and collaboration.
- [Docs](https://codesandbox.io/docs)
- [StellarAgent Sandbox](https://codesandbox.io/p/github/AReid987/stellarAgent/main)

### **Stackblitz**

#### Description

- Online development environment that runs entirely in the browser.
- [Docs](https://developer.stackblitz.com/)
- [StellarAgent Stackblitz](https://stackblitz.com/~/github.com/AReid987/stellarAgent)

### **Lightning.ai**

#### Description

- Platform for building and deploying AI-powered applications.
- [Docs](https://lightning.ai/docs/overview/getting-started)
- [StellarAgent Studio](https://lightning.ai/readmusik/vision-model/studios/stellaragent/code)

### **Project IDX**

#### Description

- Google's cloud-based development environment.
- [Docs](https://lightning.ai/docs/overview/getting-started)
- [StellarAgent IDX](https://idx.google.com/stellaragent-9530865)

### **Windsurf**

#### Description

- Modern development environment for web applications.
- [Docs](https://docs.codeium.com/windsurf/getting-started)

### **Bolt.diy**

#### Description

- Framework for building interactive CLI applications.
- [Github](https://github.com/stackblitz-labs/bolt.diy)

### **Databutton**

#### Description

- Platform for building and sharing data applications.
- [Docs](https://docs.databutton.com/)

### **Zed**

#### Description

- High-performance, multiplayer code editor.
- [Docs](https://zed.dev/docs/)

==================================

## 💡 IDE Coding Assistants

---

### **Continue**

#### Description

- AI-powered coding assistant for natural language programming.
- [GitHub Repo](https://github.com/continuedev/continue)
- [Docs](https://docs.continue.dev/)

### **Copilot Arena**

#### Description

- Competitive environment for testing and comparing AI coding assistants.
- [GitHub](https://github.com/lmarena/copilot-arena)

### **Cline**

#### Description

- Command-line interface framework with modern features.
- [GitHub](https://github.com/cline/cline)

==================================

## 🦾 Internal Agents

---

### **Browser Use && LightRAG**

#### Description

- Tools for browser automation and lightweight RAG implementations.
- [Browser Use](https://github.com/browser-use/browser-use)
- [LightRAG Docs](https://lightrag.github.io/)

### **Open Interpreter**

#### Description

- Natural language interface for executing code and system commands.
- [Docs](https://docs.openinterpreter.com/getting-started/introduction)

### **Fabric AI**

#### Description

- Framework for building and deploying AI-powered applications.
- [GitHub](https://github.com/danielmiessler/fabric)

### Pieces for Developers

#### Description

- Long term memory and context accross developer workflow environment.
- [Docs](https://pieces.app/)
-
==================================

## 💽 Database

---

### **Couchbase**

#### Description

- Distributed NoSQL database with built-in cache and SQL-like query language.
- [Couchbase](https://cloud.couchbase.com/signed-out)

### **PostgreSQL**

#### Description

- Powerful, open source object-relational database system.
- [Documentation](https://www.postgresql.org/docs/)

==================================

## ☁️ Cloud

### **Google Cloud**

#### Description

- Suite of cloud computing services for building, deploying, and scaling applications.
- [Documentation](https://cloud.google.com/docs)

### **AWS**

#### Description

- Comprehensive cloud computing platform offering over 200 services.
- [Documentation](https://docs.aws.amazon.com/)

### **Oracle**

#### Description

- Enterprise cloud computing platform with integrated services.
- [Documentation](https://docs.oracle.com/en-us/iaas/Content/home.htm)

### **IBM**

#### Description

- Enterprise-grade cloud computing platform with AI capabilities.
- [Documentation](https://www.ibm.com/docs/en)

==================================

## 📸 Image & Video Generation

---

### **Comfy UI**

#### Description

- Node-based interface for image generation and processing.
- [GitHub](https://github.com/comfyanonymous/ComfyUI)
- [Examples](https://github.com/comfyanonymous/ComfyUI_examples)
- [Docs](https://docs.comfy.org/get_started/introduction)

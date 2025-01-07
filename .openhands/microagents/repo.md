# Repository: stellarAgentRepo

Description: A web app the provides users with access to agents that can create and manage wallets and custom assets on the stellar blockchain.

## Directory Structure

Some of the significant sections of the repository

- apps/: Standalone Applications
- apps/ai-gateway/: Unified AI API, Loadbalancer, LLM router, Fallback/Retry Mechanism
- apps/docs/: App Documentation
- apps/web:/ Main Application code
- packages/: reusable internable packages

.
├──  apps
│   ├──  ai-gateway
│   ├──  cpu-ops
│   ├──  docs
│   └──  web
├──  codecov
├──  codecov.SHA256SUM
├── 󱧃 codecov.SHA256SUM.sig
├──  codecov.yml
├── config
│   └── cz.config.cjs
├── documentation
│   ├── ai-docs
│   ├── devLog
│   ├── diagrams
│   ├── pm
│   ├── repo_assets
│   └── techStack_docs
├── llama.log
├── models
│   └── picovoice
├── node_modules
├── package.json
├── packages
│   ├── agent-api
│   ├── eslint-config
│   ├── ingester
│   ├── typescript-config
│   └── ui
├── pnpm-lock.yaml
├── pnpm-workspace.yaml
├── pykanban.json
├── pyproject.toml
├── README.md
├── renovate.json
├── requirements.in
├──  requirements.txt
├──  scripts
│   ├──  aider.sh
│   └──  openhands.sh
├──  SECURITY.md
├──  stellar-blockchain-wallet-management-app-1733622008246.sql
└──  turbo.json

Setup:

- Run `pnpm install` to install dependencies
- Run `pnpm dev` for development
- Run `pnpm test` for testing

Guidelines:

- Follow Eslint configuration
- Write tests for all new features
- Use typescript for new Node or JavaScript code
- Use uv for Python package management
- Use uv instead of pip like `uv pip install`

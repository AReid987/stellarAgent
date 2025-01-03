Repository: stellarAgentRepo

Description: A web app

Directory Structure:
- apps/: Standalone Applications
- apps/ai-gateway/: Unified AI API, Loadbalancer, LLM router, Fallback/Retry Mechanism
- apps/docs/: Internal Documentation
- apps/garak/:
- apps/cpu-ops/:
- apps/web:/ Main Application code
- packages/: reusable internable packages

 .
├──  apps
│   ├──  ai-gateway
│   ├──  cpu-ops
│   ├──  docs
│   ├──  garak
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
│   ├── @codesandbox
│   ├── @eslint
│   ├── @eslint-community
│   ├── @next
│   ├── @stellar-agent
│   ├── @types
│   ├── @typescript-eslint
│   ├── cz-git -> .pnpm/cz-git@1.7.1/node_modules/cz-git
│   ├── czg -> .pnpm/czg@1.10.0/node_modules/czg
│   ├── eslint -> .pnpm/eslint@9.17.0/node_modules/eslint
│   ├── eslint-config-prettier -> .pnpm/eslint-config-prettier@9.1.0_eslint@9.17.0/node_modules/eslint-config-prettier
│   ├── eslint-plugin-only-warn -> .pnpm/eslint-plugin-only-warn@1.1.0/node_modules/eslint-plugin-only-warn
│   ├── eslint-plugin-react -> .pnpm/eslint-plugin-react@7.37.3_eslint@9.17.0/node_modules/eslint-plugin-react
│   ├── eslint-plugin-react-hooks -> .pnpm/eslint-plugin-react-hooks@5.1.0_eslint@9.17.0/node_modules/eslint-plugin-react-hooks
│   ├── eslint-plugin-turbo -> .pnpm/eslint-plugin-turbo@2.3.3_eslint@9.17.0/node_modules/eslint-plugin-turbo
│   ├── eslint-scope -> .pnpm/eslint-scope@8.2.0/node_modules/eslint-scope
│   ├── eslint-visitor-keys -> .pnpm/eslint-visitor-keys@4.2.0/node_modules/eslint-visitor-keys
│   ├── gptlint -> .pnpm/gptlint@1.6.0/node_modules/gptlint
│   ├── log-symbols -> .pnpm/log-symbols@7.0.0/node_modules/log-symbols
│   ├── prettier -> .pnpm/prettier@3.4.2/node_modules/prettier
│   ├── turbo -> .pnpm/turbo@2.3.3/node_modules/turbo
│   ├── typescript -> .pnpm/typescript@5.7.2/node_modules/typescript
│   ├── typescript-eslint -> .pnpm/typescript-eslint@8.19.0_eslint@9.17.0_typescript@5.7.2/node_modules/typescript-eslint
│   └── zx -> .pnpm/zx@8.3.0/node_modules/zx
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

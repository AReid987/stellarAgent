# AI Gateway

**App**: @stellar-agent/ai-gateway

==========================================

## This Document Explains

- System Architecture
- Information Flow
- Usage

==========================================

### Important links

...........................................

#### Coders

- 🏆 [Aider Chat](https://aider.chat/)
- Bolt.diy
- GPT Pilot
- OpenHands
- Project IDX
- Databutton
- Cline
- Blackbox

==========================================

#### AI Gateway

- DSPy:
  - Prompt Engineering
- Not Diamond: 
  - Evaluation & Recommendation Framework 
  - Intelligent model router for choosing the best model per task
- portkey-ai: 
  - Python client for Portkey
- Open Router:
  - Open source router for AI services
- Comet Opik:
  - Open source Observability platform
- Promptfoo:
  - Open source Evaluation & Benchmarking platform

==========================================

#### API Server

- fastAPI: Python Web framework
- uvicorn: ASGI server to run FastAPI
- httpx: For making HTTP requests
- python-dotenv: To manage environment variables

==========================================

### Development Environment

- Dev Containers
- Docker
- PNPM
- Turborepo

==========================================

### DX & Interfaces

- Rich: For beautiful terminal output
- typer:
- Textualize

==========================================

### CI / CD

- czg
- Commitlint
- Lint-Staged
- Lefthook
- Biome.js
- Eslint
- Prettier
- Megalinter

==========================================

#### Blockchain

- Stellar SDK

==========================================

#### LLM Inference Providers

- Gemini
- Mistral
- Open Router
- Groq
- Cerebras
- Sambanova
- Huggingface Serverless Inference
- GitHub Models API
- Together AI

==========================================

#### Cloud Providers & Hosting

- Vercel
- Netlify
- Railway
- AWS
- GCP
- IBM
- Oracle
- Cloudflare
- Cloudflare Docs
- Azure

==========================================

## Core Functionality

### Unified API Endpoint

- A single endpoint for all AI requests.

### Load Balancing

- Distribute requests across multiple LLM providers.

### Fallback and Retry Logic

- Handle failures gracefully by retrying or switching providers.

### Intelligent Routing

- Route requests to the best-suited provider/model based on:
  - task type
  - cost
  - latency
  - other metrics

### Extensibility

- Easily add new providers or models in the future.

### Monitoring and Logging

- Track performance, errors, and usage metrics.

==========================================

## Aider As An API

- Refactored Aider as a API
<!-- TODO: - User Prompt enhanced via DSPy -->

==========================================

### FastAPI Gateway

- Acts as the entry point for all requests.
- Handles authentication, rate limiting, and request validation.

### Not Diamond

- Responsible for intelligent routing.
- Routes requests to the best-suited provider/model based on cost, accuracy, and task type.

### Portkey

- Handles caching and monitoring.
- Caches responses to reduce costs and latency.
- Tracks usage, latency, and errors for each provider.

### Open Router

- Treated as another provider in the load balancer.
- Provides access to free and paid models, expanding your options.

### Other Providers

- Mistral
- Gemini
- Huggingface Serverless Inference
- Github Models API
- Groq
- Cerebras
- Sambanova

==========================================

## High Level Architecture

### Information Flow

User prompt → FastAPI Gateway → Not Diamond → Portkey → Cached? Or LLM Provider → Response → Portkey → Not Diamond → FastAPI → User

==========================================

### API Gateway Layer

- Built with FastAPI
- Exposes a single endpoint (e.g., /v1/ai/completions)
- Handles authentication, rate limiting, and request validation.

===========================================

### Load Balancer and Router

- Implements load balancing across LLM providers.
- Includes intelligent routing logic to select the best provider/model for each request.

==========================================

### Provider Adapters

- Abstracts interactions with different LLM providers (e.g., Open Router, Mistral, Gemini, etc.).
- Normalizes responses from different providers into a consistent format.

===========================================

### Fallback and Retry Mechanism

- Retries failed requests with the same or a different provider.
-Implements circuit breakers to avoid overloading failing providers.

==========================================

### Monitoring and Analytics

- Logs requests, responses, and errors.
- Tracks latency, cost, and success rates for each provider.

==========================================

## @stellar-agent/ai-gateway Documentation

### Module Overview

This module implements a FastAPI application that serves as the AI gateway for StellarAgent. It provides a simple API with a greeting message.

==========================================

### Setup

1. Install dependencies:
```bash
uv pip install -r requirements.txt
```

2. Configure environment variables:
- Copy `.env.example` to `.env`
- Add your Portkey API key to `.env`:
```
PORTKEY_API_KEY=your_portkey_api_key_here
```

### API Endpoints

#### GET /
- **Description**: Returns a greeting message.
- **Response**:
  - **200 OK**: A JSON object containing the greeting message.
    ```json
    {
      "message": "Welcome to StellarAgent AI Gateway"
    }
    ```

#### POST /v1/completions
- **Description**: Creates a completion using Portkey's unified AI gateway. This endpoint handles load balancing, caching, fallbacks, and retries across multiple LLM providers.
- **Request Body**:
  ```json
  {
    "prompt": "Your prompt text here",
    "model": "gpt-3.5-turbo"  // Optional, defaults to Portkey's default model
  }
  ```
- **Response**:
  - **200 OK**: The completion response
    ```json
    {
      "choices": [
        {
          "message": {
            "role": "assistant",
            "content": "Generated response"
          }
        }
      ]
    }
    ```
  - **500 Error**: If there's an error communicating with Portkey
    ```json
    {
      "detail": "Error message"
    }
    ```

### Development

To run the server locally:
```bash
# Install dependencies
pnpm install

# Install Python dependencies
uv pip install -r requirements.txt

# Start the development server
pnpm dev  # This runs: fastapi dev main.py
```

The API will be available at http://localhost:8000

API documentation will be available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

==========================================

### Functions

#### main()
- **Description**: Prints a greeting message to the console.
- **Usage**: This function is called when the script is executed directly.

==========================================

## Working with the Coders

#### Direct Usage

### Aider

#### Adding Files

- Add just the files you want to edit: 

```bash
   /add <file1> <file2> ...
```

#### Managing the Chat

- Keep only the files needed for the current task.
- Drop unnecessary files from the chat:

```bash
   /drop <file1> <file2> ...
```

#### Planning

- Break big tasks into smaller ones.
- Do one sub task at a time.

- Make a plan for complex tasks.
- Use the `/ask` command to discuss the plan with Aider

```bash
   /ask I want to build ...
```

#### Creating New Files

- When you want Aider to create a new file, create a new empty file and `/add` it to the chat.

#### Fixing Bugs and Tests

- To fix a bug use the `/run` command for the failing execution.

- to fix a failing test use the `/test` command.

#### Providing Docs

- Paste a URL to the chat and Aider will scrape and read the content.
- Use the `/read` command to provide the content of a file from anywhere on the local filesystem.

#### Conventions

- Add small Markdown files to the chat with conventions
- To mark as read-only and enable caching:
  - `/read CONVENTIONS.md`
  - `aider --read CONVENTIONS.md`

- [Community Conventions Repo](https://github.com/Aider-AI/conventions)

- add to `.aider.conf.yml` to always load conventions:

```yaml
  read: CONVENTIONS.md
```  

#### Copy / Paste Web Chat

- Use the `/copy-context` command to copy the chat context to the clipboard.
#### Interrupting Aider

- CTRL + C

#### Multi line input

- use the `{` and `}` characters to create multi line input.
- Paste the multi line input into the chat.
- Use the `--editor` command to edit the multi line input in your editor.

⭐ #### Watch Mode

- Use the `--watch-files` flag
- Add `watch-files: true` to your `.aider.conf.yml`` file
- Aider will watch for comments beginning or ending with `AI`
- If `AI!` is used Aider will make changes to the code
- If `AI?` is used Aider will respond to the question

#### Troubleshooting

- Use the `/clear` command to clear the chat history.
- `/drop` unnecessary files from the chat.
- Try `/ask` to create a plan before writing code.
- Try a new `/model` to see if it works better.
- Code the next step yourself, then try switching back to Aider.
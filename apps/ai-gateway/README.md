# AI Gateway

...........................................

**App**: @stellar-agent/ai-gateway

===========================================

##  This Document Explains

- System Architecture
- Information Flow

===========================================

### Important links

...........................................

#### Coders

- Aider Chat
- GPT Pilot
- OpenHands
- Bolt.diy

===========================================

#### AI Gateway

- DSPy:
- Not Diamond: Evaluation & Recommendation Framework for choosing the best model per task
- portkey-ai: Python client for Portkey
- Open Router
- Comet Opik:
- Promptfoo:

===========================================

#### API Server

- fastAPI: Python Web framework
- uvicorn: ASGI server to run FastAPI
- httpx: For making HTTP requests (Portkey
- python-dotenv: To manage environment variables

===========================================

### Development Environment

- Dev Containers
- Docker
- PNPM
- Turborepo

===========================================

### DX & Interfaces

- Rich: For beautiful terminal output
- typer:
- Textualize

===========================================

### CI / CD

- czg
- Commitlint
- Lint-Staged
- Lefthook
- Biome.js
- Eslint
- Prettier
- Megalinter

===========================================

#### Blockchain

- Stellar SDK

===========================================

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

===========================================

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

===========================================

## Core Functionality

...........................................

### Unified API Endpoint

...........................................

- A single endpoint for all AI requests.

### Load Balancing

...........................................

- Distribute requests across multiple LLM providers.

### Fallback and Retry Logic

...........................................

- Handle failures gracefully by retrying or switching providers.

### Intelligent Routing

...........................................

- Route requests to the best-suited provider/model based on:
  - task type
  - cost
  - latency
  - other metrics.

### Extensibility

...........................................

- Easily add new providers or models in the future.

### Monitoring and Logging

...........................................

- Track performance, errors, and usage metrics.

===========================================

## Aider As An API

...........................................

- Refactored Aider as a API
<!-- TODO: - User Prompt enhanced via DSPy -->

===========================================

### FastAPI Gateway:

- Acts as the entry point for all requests.
- Handles authentication, rate limiting, and request validation.

...........................................

### Not Diamond:

- Responsible for intelligent routing.
- Routes requests to the best-suited provider/model based on cost, accuracy, and task type.

...........................................

### Portkey:

- Handles caching and monitoring.
- Caches responses to reduce costs and latency.
- Tracks usage, latency, and errors for each provider.

...........................................

### Open Router:

- Treated as another provider in the load balancer.
- Provides access to free and paid models, expanding your options.

...........................................

### Other Providers:

- Mistral
- Gemini
- Huggingface Serverless Inference
- Github Models API
- Groq
- Cerebras
- Sambanova

===========================================

## High Level Architecture

### Information Flow

User prompt → FastAPI Gateway → Not Diamond → Portkey → Cached? Or LLM Provider → Response → Portkey → Not Diamond → FastAPI → User

===========================================

### API Gateway Layer

- Built with FastAPI
- Exposes a single endpoint (e.g., /v1/ai/completions)
- Handles authentication, rate limiting, and request validation.

===========================================

### Load Balancer and Router

- Implements load balancing across LLM providers.
- Includes intelligent routing logic to select the best provider/model for each request.

===========================================

### Provider Adapters

- Abstracts interactions with different LLM providers (e.g., Open Router, Mistral, Gemini, etc.).
- Normalizes responses from different providers into a consistent format.

===========================================

### Fallback and Retry Mechanism

- Retries failed requests with the same or a different provider.
-Implements circuit breakers to avoid overloading failing providers.

===========================================

### Monitoring and Analytics

- Logs requests, responses, and errors.
- Tracks latency, cost, and success rates for each provider.

===========================================

## ai-gateway Documentation

...........................................

### Module Overview

This module implements a FastAPI application that serves as the AI gateway for StellarAgent. It provides a simple API with a greeting message.

===========================================

### API Endpoints

...........................................

#### GET /
- **Description**: Returns a greeting message.
- **Response**:
  - **200 OK**: A JSON object containing the greeting message.
    ```json
    {
      "message": "Hello StellarAgent"
    }
    ```

===========================================

### Functions

...........................................

#### main()
- **Description**: Prints a greeting message to the console.
- **Usage**: This function is called when the script is executed directly.

===========================================

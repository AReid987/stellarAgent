---
type: Page
title: AI Gateway Implementation Plan
description: null
icon: null
createdAt: '2024-12-30T12:25:31.815Z'
creationDate: 2024-12-30 06:25
modificationDate: 2025-01-01 06:00
tags: []
coverImage: null
---

# AI Gateway Implementation Plan

## Portkey

[What is Portkey? - Portkey Docs](https://portkey.ai/docs/introduction/what-is-portkey)

### What?

- **Unified** AI Interface

#### Implementation Options

- SDK - Python, NodeJS

- REST API

- OpenAI SDK - Python, NodeJS

#### Latency

- 20 - 40 ms

#### Security 

- ISO:27001 & SOC 2 certified

- GDPR HIPAA compliant

- AES-256 data encryption in transit & at rest

#### Scalability

- 25M requests / day 

- 99.99% Uptime

- [Portkey Status Page](https://status.portkey.ai/)

**No timeouts imposed**

**SSO Supoorted**

#### Pricing

#### Open Source

- Free & Open Source Gateway

    [GitHub - Portkey-AI/gateway: A blazing fast AI Gateway with integrated guardrails. Route to 200+ LLM...](https://github.com/Portkey-AI/gateway)

#### Managed Free Tier

- Free Tier Managed Version 

    - 10k requests / month

### Setup

#### Get API Key

- Log in & go to Settings Page

#### Integrate

- Used Python SDK Method

- Success displayed on Portkey Dashboard

### Portkey Features

#### AI Gateway

---

[Universal API - Portkey Docs](https://portkey.ai/docs/product/ai-gateway/universal-api)

[Multimodal Capabilities - Portkey Docs](https://portkey.ai/docs/product/ai-gateway/multimodal-capabilities)

[Virtual Keys - Portkey Docs](https://portkey.ai/docs/product/ai-gateway/virtual-keys)

[Conditional Routing - Portkey Docs](https://portkey.ai/docs/product/ai-gateway/conditional-routing)

---

[Cache (Simple & Semantic) - Portkey Docs](https://portkey.ai/docs/product/ai-gateway/cache-simple-and-semantic)

[Automatic Retries - Portkey Docs](https://portkey.ai/docs/product/ai-gateway/automatic-retries)

[Request Timeouts - Portkey Docs](https://portkey.ai/docs/product/ai-gateway/request-timeouts)

[Budget Limits - Portkey Docs](https://portkey.ai/docs/product/ai-gateway/virtual-keys/budget-limits)

---

[Fallbacks - Portkey Docs](https://portkey.ai/docs/product/ai-gateway/fallbacks)

[Load Balancing - Portkey Docs](https://portkey.ai/docs/product/ai-gateway/load-balancing)

[Canary Testing - Portkey Docs](https://portkey.ai/docs/product/ai-gateway/canary-testing)

---

---

### Observability & Logs

---

[Logs - Portkey Docs](https://portkey.ai/docs/product/observability/logs)

---

[Tracing - Portkey Docs](https://portkey.ai/docs/product/observability/traces)

---

[Analytics - Portkey Docs](https://portkey.ai/docs/product/observability/analytics)

---

---

[Filters - Portkey Docs](https://portkey.ai/docs/product/observability/filters)

---

[Metadata - Portkey Docs](https://portkey.ai/docs/product/observability/metadata)

---

[Feedback - Portkey Docs](https://portkey.ai/docs/product/observability/feedback)

---

### Prompt Library

---

[Prompt Templates - Portkey Docs](https://portkey.ai/docs/product/prompt-library/prompt-templates)

---

[Prompt Partials - Portkey Docs](https://portkey.ai/docs/product/prompt-library/prompt-partials)

---

[Advanced Prompting with JSON Mode - Portkey Docs](https://portkey.ai/docs/product/prompt-library/advanced-prompting-with-json-mode)

---

---

### AI Providers

---

#### Google Gemini

[Google Gemini - Portkey Docs](https://portkey.ai/docs/integrations/llms/gemini)

---

#### Together AI

[Together AI - Portkey Docs](https://portkey.ai/docs/integrations/llms/together-ai)

---

#### Mistral AI

[Mistral AI - Portkey Docs](https://portkey.ai/docs/integrations/llms/mistral-ai)

---

---

#### Groq

[Groq - Portkey Docs](https://portkey.ai/docs/integrations/llms/groq)

---

#### Cerebras

[Cerebras - Portkey Docs](https://portkey.ai/docs/integrations/llms/cerebras)

---

#### Sambanova

[SambaNova - Portkey Docs](https://portkey.ai/docs/integrations/llms/sambanova)

---

---

#### GitHub

[Github - Portkey Docs](https://portkey.ai/docs/integrations/llms/github)

---

#### LocalAI

[LocalAI - Portkey Docs](https://portkey.ai/docs/integrations/llms/local-ai)

---

#### OpenRouter

[OpenRouter - Portkey Docs](https://portkey.ai/docs/integrations/llms/openrouter)

---

---

#### HuggingFace

[Hugging Face - Portkey Docs](https://portkey.ai/docs/integrations/llms/huggingface)

#### Jina

[Jina AI - Portkey Docs](https://portkey.ai/docs/integrations/llms/jina-ai)

---

#### Cloudflare Workers AI

[Workers AI - Portkey Docs](https://portkey.ai/docs/integrations/llms/workers-ai)

#### xAI

[xAI - Portkey Docs](https://portkey.ai/docs/integrations/llms/x-ai)

---

#### Ollama

[Ollama - Portkey Docs](https://portkey.ai/docs/integrations/llms/ollama)

---

---

### Open Source

[GitHub - Portkey-AI/gateway: A blazing fast AI Gateway with integrated guardrails. Route to 200+ LLM...](https://git.new/portkey)

### Native Integrations

---

[Langchain (Python) - Portkey Docs](https://portkey.ai/docs/integrations/libraries/langchain-python)

---

[LlamaIndex (Python) - Portkey Docs](https://portkey.ai/docs/integrations/libraries/llama-index-python)

---

[Autogen - Portkey Docs](https://portkey.ai/docs/integrations/libraries/autogen)

---

---

[Vercel - Portkey Docs](https://portkey.ai/docs/integrations/libraries/vercel)

---

[DSPy - Portkey Docs](https://portkey.ai/docs/integrations/libraries/dspy)

---

[Promptfoo - Portkey Docs](https://portkey.ai/docs/integrations/libraries/promptfoo)

---

---

### Configs

- **Create** config & Attach config ID in Client

- **Status Column** shows config in Logs

#### Config Object Documentation

- API interactions for Providers

- Load Balancing

- Fallback Strategies

#### Gateway Config Object

#### Schema

```json
{
"$schema": "http://json-schema.org/draft-07/schema#",
"type": "object",
"properties": {
  "strategy": {
    "type": "object",
    "properties": {
      "mode": {
        "type": "string",
        "enum": [
          "single",
          "loadbalance",
          "fallback"
        ]
      },
      "on_status_codes": {
        "type": "array",
        "items": {
          "type": "number"
        },
        "optional": true
      }
    }
  },
  "provider": {
    "type": "string",
    "enum": [
      "openai",
      "anthropic",
      "azure-openai",
      "anyscale",
      "cohere",
      "palm"
    ]
  },
  "resource_name": {
    "type": "string",
    "optional": true
  },
  "deployment_id": {
    "type": "string",
    "optional": true
  },
  "api_version": {
    "type": "string",
    "optional": true
  },
  "override_params": {
    "type": "object"
  },
  "api_key": {
    "type": "string"
  },
  "virtual_key": {
    "type": "string"
  },
  "cache": {
    "type": "object",
    "properties": {
      "mode": {
        "type": "string",
        "enum": [
          "simple",
          "semantic"
        ]
      },
      "max_age": {
        "type": "integer",
        "optional": true
      }
    },
    "required": [
      "mode"
    ]
  },
  "retry": {
    "type": "object",
    "properties": {
      "attempts": {
        "type": "integer"
      },
      "on_status_codes": {
        "type": "array",
        "items": {
          "type": "number"
        },
        "optional": true
      }
    },
    "required": [
      "attempts"
    ]
  },
  "weight": {
    "type": "number"
  },
  "on_status_codes": {
    "type": "array",
    "items": {
      "type": "integer"
    }
  },
  "targets": {
    "type": "array",
    "items": {
      "$ref": "#"
    }
  }
},
"anyOf": [
  {
    "required": [
      "provider",
      "api_key"
    ]
  },
  {
    "required": [
      "virtual_key"
    ]
  },
  {
    "required": [
      "strategy",
      "targets"
    ]
  },
  {
    "required": [
      "cache"
    ]
  },
  {
    "required": [
      "retry"
    ]
  }
],
"additionalProperties": false
}

```

#### Example Configs

```json
// Simple config with cache and retry
{
  "virtual_key": "***", // Your Virtual Key
  "cache": { // Optional
    "mode": "semantic",
    "max_age": 10000
  },
  "retry": { // Optional
    "attempts": 5,
    "on_status_codes": []
  }
}

// Load balancing with 2 OpenAI keys
{
  "strategy": {
      "mode": "loadbalance"
    },
  "targets": [
    {
      "provider": "openai",
      "api_key": "sk-***"
    },
    {
      "provider": "openai",
      "api_key": "sk-***"
    }
  ]
}

```

---

### Schema Details

| Key Name          | Description                     | Type             | Required                               | Enum Values                                                                                                                                                                    | Info                                              |
| :---------------- | :------------------------------ | :--------------- | :------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------ |
| `strategy`        | For the config  ​or target      | object           | Yes  ​If no `provider`\||`virtual_key` | -                                                                                                                                                                              | *Strategy Object Details*                         |
| `provider`        | Name of Provider                | string           | Yes  ​If no  ​`mode`\||`virtual_key`   | "groq", "cerebras", "sambanova", "huggingface"                                                                                                                                 | -                                                 |
| `api_key`         | API key                         | string           | Yes  ​If `provider` specified          | -                                                                                                                                                                              | -                                                 |
| `virtual_key`     | Virtual Key ID                  | string           | Yes  ​If no  ​`mode`\||**provider**    | -                                                                                                                                                                              | -                                                 |
| `cache`           | Caching Config                  | object           | No                                     | -                                                                                                                                                                              | *Cache Object Details*                            |
| `retry`           | Retry Config                    | object           | No                                     | -                                                                                                                                                                              | *Retry Object Details*                            |
| `weight`          | Load balancing ​weight          | number           | No                                     | -                                                                                                                                                                              | *Used in* `loadbalance` *mode*                    |
| `on_status_codes` | Status Code to trigger fallback | array of strings | No                                     | -                                                                                                                                                                              | *Used in* `fallbsck` *mode*                       |
| `targets`         | List of target configs          | array            | Yes  ​If `mode` specified              | -                                                                                                                                                                              | *Follow config schema*                            |
| `request_timeout` | Request timeout configs         | number           | No                                     | -                                                                                                                                                                              | -                                                 |
| `custom_host`     | Route to private ​model         | string           | No                                     | -                                                                                                                                                                              | *Used with* `provider` + `api_key`                |
| `forward_headers` | Sensitive headers               | array of strings | No                                     | -                                                                                                                                                                              | -                                                 |
| `override_params` | Pass model name + hyper params  | object           | No                                     | ”model”, “temperature”, “frequency_penalty”, “logit_bias”, “logprobs”, “top_logprobs”, “max_tokens”, “n”, “presence_penalty”, “response_format”, “seed”, “stop”, “top_p”, etc. | *Pass everything typically in the normal payload* |

### Strategy Object

| Key Name          | Description                                       | Type             | Required | Enum Values               | Info     |
| :---------------- | :------------------------------------------------ | :--------------- | :------- | :------------------------ | :------- |
| `mode`            | Strategy Mode for config                          | string           | yes      | "loadbalance", "fallback" | -        |
| `on_status_codes` | status codes to apply.  ​Only for "fallback" mode | array of numbers | no       | -                         | Optional |

### Cache Object

| Key Name  | Description              | Type    | Required | Enum Values          | Info     |
| :-------- | :----------------------- | :------ | :------- | :------------------- | :------- |
| `mode`    | Cache Mode               | string  | yes      | "simple", "semantic" | -        |
| `max_age` | Max age of cache entries | integer | no       | -                    | Optional |

### Retry Object

| Key Name          | Description                                       | Type             | Required | Enum Values | Info     |
| :---------------- | :------------------------------------------------ | :--------------- | :------- | :---------- | :------- |
| `attempts`        | Number of retries                                 | integer          | yes      | -           | -        |
| `on_status_codes` | status codes to apply.  ​Only for "fallback" mode | array of strings | no       | -           | Optional |

### Notes

- Single provider mode assumed if no `mode` key specified

    - requires `provider` + `api_key` || `virtual_key`

- `loadbalance` && `fallback` 

    - `targets` array -> configs for each target

- `cache` && `retry` objects -> additional configs

### Examples

- 

- 


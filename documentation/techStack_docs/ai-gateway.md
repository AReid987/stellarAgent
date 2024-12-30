# AI Gateway

## Core Functionality

### Unified API

- Simplified, Sinuglar API for all available Inference Providers

### Model Routing

#### Dynamic Routing

- Route requests to the appropriate Inference Provider given the factors

##### Prompt Content

- Analyze the content of the prompt to determine the best Inference Provider

##### Cost vs Quota Balance & Rate Limits

- Route to the Inference Provider that is most cost effective given the current balance and rate limits
- Consider the desired quality

##### Latency

- Prioritize speed applicable

#### Load Balancing

- Distribute requests across multiple Inference Providers to imporve performance and reliability
- Mulitple Instances of the same or different Inference Providers depending on the requirements of the request

### Observability

#### Metrics & Logging

- Track key metrics
  - Request Rate
  - Latency
  - Error Rate
  - Cost

- Log all requests and responses
  - Debugging
  - Auditing
  - Analysis

### Security

#### Authentication

- Verify the identity of the user
- Ensure the user has the necessary permissions

#### Data Privacy

- Ensure that the data is not exposed to unauthorized parties
- Encrypt data in transit and at rest

## Integration

### Portkey

- Unified API & Entry Point
- AI Gateway with guardrails

### Not Diamond

- Router & Model Gateway

### Open Router

- Dynamic Routing

### Opik

- Tracing & Evaluation
- LLM as a Judge

### Promptfoo

- TTD for LLM Development
- Prompt Analysis
- Evaluation & Benchmarking
- Red Teaming

### Weave

- Tracing & Evaluation

### Inference Providers

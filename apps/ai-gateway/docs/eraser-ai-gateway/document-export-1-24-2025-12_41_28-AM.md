# ADR: StellarAgent

---

![stellAg-floating-agent-glass.webp](https://eraser.imgix.net/workspaces/kpbXLGH20jNm1ilZDko3/aqRdiI7q3jemT78XWXQfk59ygUk2/hMvvHvms0eQxkVOdBKQgo.webp?ixlib=js-3.7.0 "stellAg-floating-agent-glass.webp")

---

## Problem Statements
---

### Inherent  + Complexity
- For even a simple **goal**, or **task**, there can be many _steps_ or _sub-tasks_. 
### Distribution of Attributes
- Currently, there is not one singular **Foundation Model,** **LLM**, **LAM,** **VLM, LVM,  **or** MLLM** that is better than _all_ the others at _every_ task
### Network Faults & Reliability
- Often, _software_ requires the **internet** in order to be useful 
- This inherently requires making **network** _requests_, and receiving **network** _responses_.
- **Network** _requests_ and _responses_ can and will **fail** a certain _percentage_ of times.
### Expensiveness = (Agents + Autonomy) * Cost
- **Agents **achieve**  goals **at a _higher_ rate and _increased _**cost**
-  As **Agents** gain in _capability_, they **increase** in their: 
    - **resilience**** **
    - usage of **tools**
    - **autonomy**
#### **Resilience **
- **Agent** responds to a **failed** _step_ or _sub-task_ by **retrying** or **pivoting** to try something else
- **Result -> **_ higher_ **success** rate at achieving **goals**
#### **Tool Use**
- **Agent **may have bespoke _functions_, make calls to _APIs, _or even call or create other **Agents**
    - The _side effect_ is more **network** _requests_, _steps_ and a _higher_ **cost.**
- **Structured Output **-> Better responses_ _are received from **tools, **increasing **success** rate
#### **Autonomy**
- **Agent **may gain in reasoning, decision making, and tool use for a _higher _**success **rate
- **Result -> **_higher _**success **rate at a _higher _**cost**
---

### Summary
- A **solution** is required to **address:** 
    - The inherent **complexity** of **Agents** accomplishing **tasks** with pseudo **Autonomy**
    - Selecting the best **Model** for each _Step_ or _Sub Task_
    - The prevalence of **errors** and **faults** in **Networking**
---

## Proposed Solutions
---

### Complexity
#### Unified AI API
- **Technology**
    - Portkey 
    - Not Diamond
    - Open Router
    - FastAPI
- **Application**
    - One interface for all **Modalities** and **Providers**
        - **Modalities**:  text, vision, audio, etc 
        - **Providers**: Mistral, OpenRouter, Gemini, etc
#### Compositional Prompt Modules
- **Technology **
    - **DSPy** -> Declarative Self Improving Python
    - **Portkey** -> Prompt Templates & Partials 
    - **Promptfoo **-> Evaluation & Benchmarking
- **Application**
    - **Programmatic** Prompting over long form written prompts
    - **Modularize** Prompts
    - **Evaluate** & **Iterate** using _repeatable_ **metrics** & methodologies
#### Architect / Editor Method
- **Technology**
    - **Aider**
    - **GPT Pilot**
    - **OpenHands**
- **Application**
    -  **Aider **
        - Architect / Editor Method
        - Diff Editor
        - Watch Files
        - Repo Map
        - Tightly coupled Git Integration
    - **GPT Pilot**
        - Architect Project Descriptions
        - Orchestrator Method
        - Multi Agent Team of Specialists
        - SQLite DB for 
            - Prompt / Response
            - Agent Actions
            - Files & metadata
    - **OpenHands**
        - UI
        - Multi Agent Autonomy
#### Orchestration
- **Technology**
    - **GPT Pilot**
    - **OpenHands**
- **Application**
    - **GPT Pilot **
        - Has an excellent project kickoff 
        - Generates and Maintains a task list
        - Many Specialized Agents each do a type of task well
    - **Orchestrator **
        - Reasoning Model delegates task to best suited Agent
- **OpenHands**
    -  UI makes it easy to know which agent is currently working
    - Output indicates when switching occurs
#### Observability
- **Technology**
    - **Portkey**
    - **Not Diamond**
    - **Opik**
    - **Posthog**
    - **OpenLit**
- **Application**
    - Each has specific observability advantages to be leveraged
### Distribution of Attributes
- **Technology**
    - **Not Diamond**
    - **Portkey**
- **Application**
    - **Not Diamond **-> Intelligent model routing
    - **Portkey **-> Loadbalancer & Virtual Keys
### Networking Reliability
- **Technology**
    - **Portkey**
- **Application**
    - Fallbacks
    - Automatic Retries
### Expensiveness
- **Technology**
    - **Portkey**
    - **Not Diamond**
    - **DSPy**
- **Application**
    - **Portkey **-> Caching
    - **Not Diamond **-> Choose cheaper model when possible
    - **DSPy **-> Caching
---

## Terminology
> [!INFO]

> These terms have some overlap. 

> Each is a specific technology or application. 

> Understanding them in context is essential.

---

### LLM (Large Language Model)
- **Description**: 
    - Large Language Models are trained on vast amounts of text data
    - LLMs perform natural language processing (NLP) tasks. 
    - An example is the GPT (Generative Pre-trained Transformer) series.
- **Uses**:
    -  Text generation, summarization, question answering, translation, etc. 
### VLM (Vision-Language Model)
- **Description**: 
    - Models that handle both visual and textual information
    - Capable of processing text related to images and videos. 
    - For example, they generate image captions or perform visual question answering (VQA).
- **Uses**: 
    - Image captioning, image search, visual question answering, etc.
### LVM (Latent Variable Model)
- **Description**: 
    - Latent Variable Models assume latent variables behind observed data
    - LVMs use the latent variables to model the data. 
    - Typical examples include Gaussian Mixture Models (GMM) and Variational Autoencoders (VAE).
- **Uses**: 
    - Data clustering, generative models, anomaly detection, etc.
### LMM (Linear Mixed Model)
- **Description**: 
    - Linear Mixed Models include both fixed effects and random effects, 
    - Effects are applied to hierarchical structures and correlated data.
- **Uses**: 
    - Data analysis in biostatistics, economics, psychology, etc.
### MLLM (Multilingual Language Model)
- **Description**: 
    - Multilingual Language Models are trained in multiple languages 
    - MLLMs perform tasks such as translation and NLP across different languages.
- **Uses**: 
    - Multilingual translation, multilingual question answering, multilingual text generation, etc.
### Generative AI
- **Description**: 
    - Generative AI refers to AI technologies that generate new data 
    - GenAI can generate different types of data includign images, text, speech, and video. 
    - This includes techniques like GANs (Generative Adversarial Networks) and VAEs.
- **Uses**: 
    - Image generation, text generation, speech synthesis, data augmentation, etc.
### Foundation Model
- **Description**: 
    - Foundation Models are large-scale, pre-trained models
    - Foundation Models can be adapted to a wide range of tasks. 
    - They serve as a base for various downstream tasks.
- **Uses**: 
    - Diverse NLP tasks, visual recognition, generative tasks, etc.
---






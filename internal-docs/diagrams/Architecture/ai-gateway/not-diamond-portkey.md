# Conceptual Architecture

- **Aider Interaction**: 
  - Aider will send prompts to your AI Gateway.
- **Not Diamond**: 
  - Your AI Gateway will interact with Not Diamond to determine the best model for each request, potentially adding metadata about the request.
- **Portkey**: 
  - Your AI Gateway will use Portkey for prompt routing, load balancing, caching, retries, fallbacks, and observability.

## Key Considerations

- **Model Selection**: 
  - Not Diamond will handle the dynamic selection of the most appropriate model.
- **Prompt/Response Caching**: 
  - Portkey will handle this at the Gateway level.
- **Load Balancing & Fallbacks**: 
  - Not Diamond will work in tandem with Portkey to intelligently route requests and manage fallbacks.
- **Observability**: 
  - Portkey will be the primary tool for observing traffic and performance.
- **Aider Interaction**: 
  - The user will be interating with Aider, and Aider will be sending requests to this AI gateway.
- **Not Diamond Interaction**: 
  - The AI Gateway will have to make requests to Not Diamond.
- **Portkey Interaction**: 
  - The AI Gateway will be using portkey.

<!-- Sepeculative. Requires further research and planning -->
<!-- DO NOT IMPLEMENT Before validation. Some details may need to be changed -->
### Initial Actions

#### AI Gateway:

- We will change the ai-gateway code to allow requests to Not Diamond as well as Portkey.
- We will change the ai-gateway code to route requests to Not Diamond first, and then use Portkey to route them to the appropriate LLM.
- We will add functionality to the ai gateway to perform additional calls to Portkey when required.

### Implementation

#### Not Diamond Integration:

- We will add code to integrate a Not Diamond client within the AI Gateway.
- We will write a separate client file for Not Diamond.
- We will call it not_diamond_client.py
- We will update the ai-gateway to allow requests to Not Diamond.
- We will add code to call Not Diamond and forward the response to Portkey.

#### Portkey Integration:

- We will update the AI Gateway's main.py to include Portkey.
- We will create a portkey_client.py
- We will add a client for Not Diamond not_diamond_client.py.
- We will create a new prompt_request.py file, to allow requests to Not Diamond.
- We will make changes to the ai gateway code to allow requests to Not Diamond first, and then to Portkey.
- We will change the PromptRequest model in main.py to make it easier to make requests to Not Diamond.
- We will update main.py to handle the Not Diamond integration.

#### Aider Interaction:

- We will make changes to allow interaction with Aider.

### Next Steps:

- **Create not_diamond_client.py**: 
  - I will create a new file not_diamond_client.py to contain the logic for communicating with Not Diamond.
- **Create portkey_client.py**: 
  - I will create a new file portkey_client.py to contain the logic for communicating with Portkey.
- **Modify main.py**: 
  - I will modify main.py to integrate Not Diamond and Portkey.
- **Add dependencies:** 
  - I will add the necessary dependencies to the ai gateway.
- **Add logic**: 
  - I will add the logic to call Not Diamond and forward the response to Portkey.
- **Add tests**: 
  - I will create test to make sure everything is working.
- **Add not_diamond_client.py**: 
  - I will add the not_diamond_client to the ai gateway, as well as logic to select the best model.
- **Add portkey_client.py**: 
  - I will add the portkey_client to the ai gateway, as well as logic to handle portkey requests.
- **Create prompt_request.py**: 
  - I will create the prompt_request.py file.
- **Modify main.py**: 
  - I will modify main.py to integrate Not Diamond and Portkey.
- **Modify ai-gateway**: 
  - I will modify the ai gateway to add the new PromptRequest.

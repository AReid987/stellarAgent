from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.portkey.portkey_client import PortkeyClient
from apps.ai_gateway.src.not_diamond.not_diamond_client import NotDiamondClient
import os

app = FastAPI(title="AI Gateway")

# Request model
class PromptRequest(BaseModel):
    prompt: str
    model: str = "not-diamond-model"  # Set the model name to your Not Diamond model's identifier in Portkey
    config: str = os.getenv("PORTKEY_CONFIG")  # Optional config ID for Portkey
    metadata: dict = None  # Optional metadata for Portkey
    trace_id: str = None
    span_id: str = None
    span_name: str = None


@app.post("/chat/not-diamond-portkey")
async def chat_with_not_diamond_portkey(request: PromptRequest):
    try:
        selected_model = NotDiamondClient().select_model()
        response = PortkeyClient().chat_completion(
            messages=[{"role": "user", "content": request.prompt}],
            model_name=selected_model,
            config_id=request.config,
            metadata=request.metadata,
            span_id=request.span_id,
            span_name=request.span_name,
            trace_id=request.trace_id,
        )
        return {"response": response, "selected_model": selected_model}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/")
async def read_root():
    """Return a greeting message."""
    return {"message": "Welcome to StellarAgent AI Gateway"}


@app.post("/v1/completions")
async def create_completion(request: PromptRequest):
    """
    Create a completion using Portkey.

    This endpoint receives prompts from developers and forwards them to Portkey,
    which handles load balancing, caching, fallbacks, and retries across multiple LLM providers.

    Args:
        request (PromptRequest): The prompt request containing the input text and optional model name

    Returns:
        dict: The completion response from the LLM provider

    Raises:
        HTTPException: If there's an error communicating with Portkey
    """
    try:
        # Format the message for Portkey
        messages = [{"role": "user", "content": request.prompt}]

        # Send the request to Portkey for completion.
        portkey_client = PortkeyClient()

        response = portkey_client.chat_completion(
            messages=messages,
            model_name=request.model,  # Portkey can use this for routing if configured
            config_id=request.config,
            metadata=request.metadata,
            span_id=request.span_id,
            span_name=request.span_name,
            trace_id=request.trace_id,
        )

        # Logic to call Not Diamond (replace with actual Not Diamond client call)
        # For now, let's just return a placeholder response
        return {
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": f"Response from Not Diamond for prompt: {request.prompt}",
                    }
                }
            ]
        }
        # Return the response in a standardized format
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def main():
    # AI Use typer to start up the AI Gateway 
    # AI It should start a CLI interface for users to select initial options for the AI Gateway
    # AI The CLI should include options for:
    # AI - FastAPI only
    # AI - FastAPI + TUI
    # AI - TUI only
    # AI For later, we can add options for:
    # AI - Aider Configurations
    # AI - API Key Management
    # AI - Logging
    # AI - Working history AI!
     
    print("AI Gateway initialized with Portkey client!")
 

if __name__ == "__main__":
    main()

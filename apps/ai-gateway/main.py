from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from portkey.portkey_client import PortkeyClient
from not_diamond.not_diamond_client import NotDiamondClient
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

        # Return the response in a standardized format
        return {
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": response
                    }
                }
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def main():    
    print("AI Gateway initialized with Portkey client!")
  
if __name__ == "__main__":
    main()

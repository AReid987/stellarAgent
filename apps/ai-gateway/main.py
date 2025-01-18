import sys
import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.portkey.portkey_client import PortkeyClient
portkey_client = PortkeyClient()

app = FastAPI(title="AI Gateway")

# Request model
class PromptRequest(BaseModel):
    prompt: str
    model: str = None  # Optional model name
    config: str = None # Optional config ID for Portkey
    metadata: dict = None # Optional metadata for Portkey
    trace_id: str = None
    span_id: str = None
    span_name: str = None

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
        
        # Get completion from Portkey client.
        # Portkey will handle caching, fallbacks, and retries based on its configuration.
        response, from_cache = portkey_client.chat_completion(
            messages=messages,
            model_name=request.model,  # Portkey can use this for routing if configured
            config_id=request.config,
            metadata=request.metadata,
            span_id=request.span_id,
            span_name=request.span_name,
        )

        if from_cache:
            # Return the cached response
            return {"choices": [{"message": {"role": "assistant", "content": response}}]}
        else:
            # Logic to call Not Diamond (replace with actual Not Diamond client call)
            # For now, let's just return a placeholder response
            return {"choices": [{"message": {"role": "assistant", "content": f"Response from Not Diamond for prompt: {request.prompt}"}}]}
        # Return the response in a standardized format
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def main():
    """Print a greeting message."""
    if len(sys.argv) > 1 and sys.argv[1] == "tui":
        from apps.ai-gateway.tui import TuiApp
        TuiApp().run()
    else:
        print("AI Gateway initialized with Portkey client!")
    # To lint this package, run: pnpm lint --filter=ai-gateway

if __name__ == "__main__":
    main()

from notdiamond import NotDiamond

from apps.ai_gateway.src.not_diamond.not_diamond_client import NotDiamondClient
client = NotDiamond()

llm_providers = [
    "openrouter/google/gemini-2.0-flash-thinking-exp-1219:free",
    "openrouter/google/gemini-2.0-flash-exp:free",
    "openrouter/meta-llama/llama-3.1-405b-instruct:free",
    "openrouter/google/gemini-flash-1.5-exp",
    "openrouter/google/gemini-exp-1206:free",
    "openrouter/meta-llama/llama-3.2-3b-instruct:free",
    "openrouter/google/gemini-flash-1.5-8b-exp",
    "openrouter/meta-llama/llama-3.1-70b-instruct:free",
    "openrouter/microsoft/phi-3-medium-128k-instruct:free",
    "openrouter/microsoft/phi-3-mini-128k-instruct:free",
    "google/gemini-2.0-flash-exp",
    "google/gemini-1.5-flash",
    "google/gemini-1.5-flash-8b",
    "google/gemini-1.5-pro",
    "google/gemini-2.0-flash-thinking-exp-1219",
    "mistral/mistral-large-latest",
    "mistral/pixtral-large-latest",
    "mistral/codestral/mamba-latest",
    "mistral/open-mistral-nemo",
    "mistral/ministral/ministral-8b-latest",
    "mistral/open-mixtral-8x22b",
    "cerebras/llama3.1/llama3.1-8b",
    "cerebras/llama3.3/llama3.3-70b",
    "sambanova/Qwen2.5-Coder-32B-Instruct",
    "sambanova/QwQ-32B-Preview",
    "sambanova/Meta-Llama-3.1-405B-Instruct",
    "sambanova/Meta-Llama-3.1-70B-Instruct",
    "sambanova/Meta-Llama-3.1-8B-Instruct",
    "sambanova/Meta-Llama-3.3-70B-Instruct",
    "sambanova/QwQ-32B-Preview",
    "sambanova/Qwen2.5-Coder-32B-Instruct",
    "groq/llama-3.3-70b-versatile",
    "groq/llama-3.3-70b-specdec",
    "groq/llama-3.2-11b-vision-preview",
    "groq/llama-3.1-8b-instant",
    "groq/mixtral-8x7b-32768",
    "groq/llama-3.2-3b-preview",
    "together_ai/meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    "together_ai/black-forest-labs/FLUX.1-schnell-Free",
    "together_ai/meta-llama/Llama-Vision-Free",
]

def main():
    not_diamond_client = NotDiamondClient()
    messages = [{"role": "user", "content": "Write a python function to calculate the factorial of a number."}]
    selected_model = not_diamond_client.select_model(messages=messages)
    print(f"Selected model: {selected_model}")

if __name__ == "__main__":
    main()

from notdiamond import NotDiamond

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


# AI Based on these docs https://docs.notdiamond.ai/docs/model_select-vs-create
# AI and the fact that I want to use a custom set of models not explicitly listed in the docs
# AI it seems that I would need to use the `model_select` method to select the best model
# AI i am not sure if we need a set of training data to use this method
# AI this section of the docs also seem to be useful and relevant to the use case of this ai gateway https://docs.notdiamond.ai/docs/real-time-personalization
# Write the plan, then the tests, then the code to pass the tests and satisfy the plan AI!

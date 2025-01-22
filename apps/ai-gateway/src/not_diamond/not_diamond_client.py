from apps.ai_gateway.src.not_diamond.main import llm_providers

class NotDiamondClient:
    def __init__(self):
        self.llm_providers = llm_providers

    def select_model(self):
        # Basic model selection: return the first model in the list
        return self.llm_providers[0]

not_diamond_client = NotDiamondClient()

if __name__ == "__main__":
    print(f"Selected model: {not_diamond_client.select_model()}")

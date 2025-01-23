import os
from notdiamond import NotDiamond

from apps.ai_gateway.src.not_diamond.main import llm_providers

class NotDiamondClient:
    def __init__(self):
        self.client = NotDiamond(
            api_key=os.getenv("NOTDIAMOND_API_KEY"),
        )

    def select_model(self, messages):
        session_id, provider = self.client.chat.completions.model_select(
            messages=messages, model=llm_providers
        )
        return provider

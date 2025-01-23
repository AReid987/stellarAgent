from not_diamond.main import llm_providers

class NotDiamondClient:
    def __init__(self):
        self.llm_providers = llm_providers
        self.client = NotDiamond()

    def select_model(self, messages):
        """
        Selects a model using Not Diamond's model_select method.

        Args:
            messages (list): A list of message dictionaries for the conversation.

        Returns:
            str: The selected model provider.
        """
        session_id, provider = self.client.chat.completions.model_select(messages=messages, model=self.llm_providers)
        return provider

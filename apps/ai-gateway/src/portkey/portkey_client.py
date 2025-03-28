import os

from dotenv import load_dotenv
from portkey_ai import Portkey

load_dotenv()

class PortkeyClient:
    def __init__(self):
        self.portkey = Portkey(
            api_key = os.getenv("PORTKEY_API_KEY"),
            config = os.getenv("PORTKEY_CONFIG"),
        )

    def chat_completion(self, messages, model_name=None, metadata=None, span_id=None, span_name=None, trace_id=None, config_id=None):
        response = self.portkey.chat.completions.create(
            messages = messages,
            # model = model_name, #Optional model name
            config = config_id,
            metadata = metadata,
            spanId = span_id,
            spanName = span_name,
            traceId = trace_id,
        )

        return response.choices[0].message.content

portkey_client = PortkeyClient()

if __name__ == "__main__":
    messages = [
        {"role": "user", "content": "Say hello."},
    ]
    chat_response = portkey_client.chat_completion(messages)
    print(chat_response)

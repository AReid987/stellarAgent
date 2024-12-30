import os

from fastapi import FastAPI

# pip install portkey_ai
from portkey_ai import Portkey

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello StellarAgent"}


def main():
    print("Hello from ai-gateway!")


# Construct a client with a virtual key
portkey = Portkey(
    api_key=os.getenv("PORTKEY_API_KEY"),
    virtual_key="mistral-virtual-85de2d",
)
completion = portkey.chat.completions.create(
    messages=[{"role": "user", "content": "What is Portkey"}],
    model="mistral-tiny",
    max_tokens=64,
)
print(completion)

if __name__ == "__main__":
    main()

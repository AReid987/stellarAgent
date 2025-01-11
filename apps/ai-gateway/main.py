from fastapi import FastAPI

app = FastAPI()

"""Return a greeting message.

This is the root endpoint of the API.
It returns a JSON object with a greeting message.

Returns:
    dict: A dictionary containing the message.
"""


@app.get("/")
async def read_root():
    return {"message": "Hello StellarAgent"}


"""
Print a greeting message.

This function prints a greeting message to the console.
"""


def main():
    print("Hello from ai-gateway!")


if __name__ == "__main__":
    main()

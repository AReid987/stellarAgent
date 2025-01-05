from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello StellarAgent"}


def main():
    print("Hello from ai-gateway!")

if __name__ == "__main__":
    main()

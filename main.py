from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def print_welcome():
    return {
        "message": "Welcome to the MINI-RAG-APP"
        }

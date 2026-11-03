
from fastapi import FastAPI

app = FastAPI(title="My First AI API")


@app.get("/")
def home():
    return {"message": "Hello, AI Engineer!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}

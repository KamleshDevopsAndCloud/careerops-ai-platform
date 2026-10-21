
from fastapi import FastAPI

app = FastAPI(
    title="CareerOps API",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "careerops-api"
    }


@app.get("/")
def root():
    return {
        "application": "CareerOps",
        "version": "0.1.0"
    }

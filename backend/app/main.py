from fastapi import FastAPI

from utils.logger import logger

logger.info("PulseFlow Started")

app = FastAPI(
    title="PulseFlow API",
    description="AI Powered Workflow Orchestration Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to PulseFlow 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
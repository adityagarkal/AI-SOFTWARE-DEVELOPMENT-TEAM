import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="AI Software Development Team — AI Service",
    description="Multi-agent orchestration service powered by LangGraph, Google Gemini, and ChromaDB.",
    version="1.0.0",
)

# Enable CORS for Next.js frontend and NestJS backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {
        "service": "AI Software Development Team - AI Service",
        "status": "online",
        "version": "1.0.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "services": {
            "fastapi": "operational",
            "langgraph": "ready",
            "gemini": "configured" if os.getenv("GEMINI_API_KEY") else "missing_key",
        },
    }


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)

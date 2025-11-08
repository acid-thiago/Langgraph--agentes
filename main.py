from fastapi import FastAPI

app = FastAPI(title="LangGraph API", version="1.0.0")

@app.get("/")
def root():
    return {
        "message": "API Online!",
        "status": "ok",
        "version": "1.0.0"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

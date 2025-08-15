from typing import Dict

from fastapi import FastAPI


app = FastAPI(title="FastAPI Project", version="0.1.0")


@app.get("/", summary="Simple test endpoint")
def read_root() -> Dict[str, str]:
    return {"message": "Fastapi With hot reload"}


@app.get("/health", summary="Health check")
def health() -> Dict[str, str]:
    return {"status": "ok"}
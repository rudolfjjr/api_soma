# -*- coding: utf-8 -*-
# api/main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Sum API")


class AddRequest(BaseModel):
    a: float
    b: float


class AddResponse(BaseModel):
    a: float
    b: float
    result: float


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/add", response_model=AddResponse)
async def add_numbers(req: AddRequest):
    """Recebe {"a": <num>, "b": <num>} e retorna soma."""
    res = req.a + req.b
    return AddResponse(a=req.a, b=req.b, result=res)
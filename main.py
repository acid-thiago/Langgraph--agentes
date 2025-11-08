from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensagem": "Olá! Eu sou o LangGraph! 🤖"}

@app.get("/health")
def saude():
    return {"status": "funcionando"}

@app.post("/perguntar")
def perguntar(pergunta: dict):
    texto = pergunta.get("texto", "")
    return {
        "resposta": f"Você disse: {texto}",
        "robo": "Robô Simples"
    }

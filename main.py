from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def raiz():
    return{"mensagem":"API FastAPI Funcionario."}
@app.get("/health")
def health():
    return{"status":"ok"}

@app.get("/soma")
def soma(a: int, b:int):
    return{"resultado":a+b}
    
from pydantic import BaseModel
class Tarefa(BaseModel):
    titulo:str
    conclida:bool = False

@app.post("/tarefa")
def criar_tarefa(tarefa:Tarefa):
    return{
        "mensagem":"tarefa recebida com sucesso",
        "dados":tarefa 
    }
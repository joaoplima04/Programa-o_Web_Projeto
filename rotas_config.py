from fastapi import APIRouter

rotas = APIRouter()

@rotas.get('/olá')
def rota1():
    return "olá mundo"

@rotas.get('/')
def rota1():
    a = 4
    b = 6
    c = 8
    return {"a": a, "b": b, "c": c}
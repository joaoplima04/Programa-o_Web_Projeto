from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from rotas_config import rotas

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home() -> HTMLResponse:
    with open('index.html', mode='r', encoding='utf-8') as arq:
        conteudo = arq.read()
    return HTMLResponse(conteudo)

uvicorn.run(app=app)
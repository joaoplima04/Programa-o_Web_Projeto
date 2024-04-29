from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cadastro", response_class=HTMLResponse)
async def cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/carrinho", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("carrinho.html", {"request": request})

@app.get("/pratos", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("pratos.html", {"request": request})

@app.get("/pratos_sobremesa", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("pratos_sobremesa.html", {"request": request})

uvicorn.run(app=app)
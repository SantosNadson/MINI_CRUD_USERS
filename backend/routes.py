from main import app
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
import json
import pandas as pd
import services

templates = Jinja2Templates(directory='frontend/templates')
app.mount("/static", StaticFiles(directory='frontend/static'), name="static")

@app.get("/")
def homepage(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/home")
def homepage(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/users")
def obter_dados(request: Request):
    return templates.TemplateResponse("users.html", {"request": request})

@app.get("/users/dados")
def mostrar_dados():
    dados = services.get_data()
    return dados

@app.post("/users/insert_dados")
async def insert_dados(request: Request):
    dados = await request.json()
    services.insert_data(dados['nome'],dados['idade'])
    return {'status':'ok'}

@app.put("/users/update_dados")
async def update_dados(request: Request):
    dados = await request.json()
    services.update_data(dados["user_id"],dados["new_name"],dados["new_age"])
    return{"usuário atualizado": "ok"}

@app.delete("/users/delete_dados")
async def delete_dados(request: Request):
    dados = await request.json()
    services.delete_data(dados["user_id"])
    return {"Usuário removido": "ok"}


if __name__ == "__main__":
    pass
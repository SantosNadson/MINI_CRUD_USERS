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
def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/home")
def home_route(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/users")
def obter_dados(request: Request):
    return templates.TemplateResponse("users.html", {"request": request})

@app.get("/users/dados")
def show_data():
    data = services.get_data()
    return data

@app.post("/users/insert_dados")
async def insert_user(request: Request):
    data = await request.json()
    services.insert_data(data['nome'], data['idade'])
    return {'status': 'ok'}

@app.put("/users/update_dados")
async def update_user(request: Request):
    data = await request.json()
    services.update_data(data["user_id"], data["new_name"], data["new_age"])
    return {"usuário atualizado": "ok"}

@app.delete("/users/delete_dados")
async def delete_user(request: Request):
    data = await request.json()
    services.delete_data(data["user_id"])
    return {"Usuário removido": "ok"}


if __name__ == "__main__":
    pass
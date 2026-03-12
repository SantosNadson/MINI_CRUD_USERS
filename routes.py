from main import app
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
import json
import pandas as pd
import services
from pydantic import BaseModel


templates = Jinja2Templates(directory="./templates")
app.mount("/static", StaticFiles(directory="./static"), name="static")

"""
========================================================================================================
========================================SUMÁRIO=========================================================
========================================================================================================
0.SEÇÃO DEDICADA AS DEFINIÇÕES DE OBJETOS
1.SEÇÃO DEDICADA AOS MÉTODOS GET
2.SEÇÃO DEDICADA AOS MÉTODOS POST
3.SEÇÃO DEDICADA AOS MÉTODOS UPDATE
4.SEÇÃO DEDICADA AOS MÉTODOS DELETE
========================================================================================================
========================================================================================================
========================================================================================================
"""
"""0.SEÇÃO DEDICADA AS DEFINIÇÕES DE OBJETOS"""

class table_users(BaseModel):
    nome: str
    idade: int | None = None
    id: int

#========================================================================================
#========================================================================================
"""1.SEÇÃO DEDICADA AOS MÉTODOS GET"""

@app.get("/")
def homepage(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/home")
def homepage(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/users")
def obter_tarefas(request: Request):
    return templates.TemplateResponse("users.html", {"request": request})

@app.get("/users/dados")
def mostrar_tarefas():
    dados = services.get_data()
    return dados

#========================================================================================
#========================================================================================
"""2.SEÇÃO DEDICADA AOS MÉTODOS POST"""

@app.post("/users/insert_dados")
async def insert_dados(request: Request):
    dados = await request.json()
    services.insert_data(dados['nome'],dados['idade'])
    return {'status':'ok'}

#========================================================================================
#========================================================================================
"""3.SEÇÃO DEDICADA AOS MÉTODOS PUT & PATCH"""

@app.post("/users/update_dados")
async def update_dados(request: Request):
    dados = await request.json()
    services.update_data(dados["user_id"],dados["new_name"],dados["new_age"])
    return{"usuário atualizado": "ok"}

#========================================================================================
#========================================================================================
"""4.SEÇÃO DEDICADA AOS MÉTODOS DELETE"""

@app.post("/users/delete_dados")
async def delete_dados(request: Request):
    dados = await request.json()
    services.delete_data(dados["user_id"])
    return {"Usuário removido": "ok"}





if __name__ == "__main__":
    pass
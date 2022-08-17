from fastapi import FastAPI
from extrair_dados_planilha import lista_de_carros

app = FastAPI()


@app.get('/')
def home():
    return {'Menssagem':'Minha primeira API'}

@app.get('/carros')
def carros():
    return {'Total':f'{len(lista_de_carros)}'}

@app.get('/carro/{id}')
def get_produto(id: int):
    return lista_de_carros[id]

@app.get('/total')
def get_todos_os_carros():
    return lista_de_carros


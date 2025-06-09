from fastapi import FastAPI, HTTPException
from models import Usuario, Produto, Loja, Pedido, Avaliacao
from typing import List

app = FastAPI()

usuarios:List[Usuario] = []
produtos: List[Produto] = []
pedidos:List[Pedido] = []
avaliacoes:List[Avaliacao] = []

lojas:List[Loja] = []


# listar lojas
@app.get("/lojas", response_model=List[Loja])
def listar_lojas():
    return lojas

#buscar loja
@app.get("/lojas/{nome}", response_model=Loja)
def listar_lojas(nome:str):
    for loja in lojas:
        if loja.nome == nome:
            return loja

    raise HTTPException(404, "Não encontrado")

#cadastrar loja
@app.post("/lojas")
def cadastrar_lojas(nome:str,descricao:str,logo:str):
    loja = Loja(
        id=len(lojas) + 1,
        nome=nome,
        descricao=descricao,
        logo=logo,
        produtos=[],
        usuarios=[],
        pedidos=[],
        avaliacoes=[]
    )
    lojas.append(loja)

#excluir loja
@app.delete("/lojas/{nome}", response_model=Loja)
def excluir_lojas(nome:str):
    for id,loja in enumerate(lojas):
        if loja.nome == nome:
            lojas.pop(id)
            return loja

    raise HTTPException(404, "Não encontrado")
    

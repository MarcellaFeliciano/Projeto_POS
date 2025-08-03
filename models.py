from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List, Optional

class Usuario(BaseModel):
    username: str
    password: str
    email: str

class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    quantidade_em_estoque: int
    categoria: str
    imagens: List[str]


class Pedido(BaseModel):
    id: int
    usuario: Usuario
    produtos: List[Produto]
    data_pedido: date
    status: str 
    endereco_entrega: str
    forma_pagamento: str

class Avaliacao(BaseModel):
    id:int
    usuario: Usuario
    produto: Produto
    nota: int  
    comentario: Optional[str]
    data_avaliacao: date

class Loja(BaseModel):
    id: int
    nome: str
    descricao: str
    logo: str
    produtos: List[Produto]
    pedidos: List[Pedido]
    avaliacoes: List[Avaliacao]
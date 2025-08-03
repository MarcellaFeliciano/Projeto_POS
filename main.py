from fastapi import FastAPI, HTTPException
from models import Usuario, Produto, Loja, Pedido, Avaliacao
from typing import List
import datetime

app = FastAPI()

usuarios:List[Usuario] = []

user_logado = Usuario(
        username='',
        password='',
        email=''
    )


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

            for num, loja in enumerate(lojas):
                loja.id = num+1

            return loja

    raise HTTPException(404, "Não encontrado")


# listar user
@app.get("/usuarios", response_model=List[Usuario])
def listar_usuarios():
    return usuarios

#buscar user
@app.get("/usuarios/{username}", response_model=Usuario)
def listar_usuario(username:str):
    for user in usuarios:
        if user.username == username:
            return user

    raise HTTPException(404, "Não encontrado")

#cadastrar user
@app.post("/usuarios")
def cadastrar_usuarios(username:str,password:str,email:str):
    user = Usuario(
        username=username,
        password=password,
        email=email
    )
    usuarios.append(user)
    user_logado.username = username
    user_logado.password = password
    user_logado.email = email

#login
@app.post("/login", response_model=str)
def login_usuarios(email:str,password:str):
    for user in usuarios:
        if user.email == email:
            if user.password == password:
                user_logado.username = user.username
                user_logado.password = user.password
                user_logado.email = user.email

    if user_logado.username == '':
        return 'erro ao logar'
    else:
        return 'login feito'
    
#logout
@app.get("/logout", response_model=Usuario)
def logout_usuarios():
    user_logado = Usuario(
            username='',
            password='',
            email=''
        )
    return user_logado
    
    raise HTTPException(404, "erro no logout")

#excluir user
@app.delete("/usuarios/{username}", response_model=Usuario)
def excluir_usuarios(username:str):
    for id,user in enumerate(usuarios):
        if user.username == username:
            usuarios.pop(id)

            return user

    raise HTTPException(404, "Não encontrado")


# buscar produtos
@app.get("/produtos", response_model=List[Produto])
def listar_produtos(nome_loja:str):
    for loja in lojas:
        if loja.nome == nome_loja:
            return loja.produtos
    raise HTTPException(404,"Não localizado.")

#buscar produto
@app.get("/produtos/{nome}", response_model=Produto)
def buscar_produto(nome_loja:str,nome: str):
    for loja in lojas:
        if loja.nome == nome_loja:
            for produto in loja.produtos:
                if produto.nome == nome:
                    return produto
    raise HTTPException(404, "Produto não encontrado")

# cadastrar produto
@app.post("/produtos", response_model=Produto)
def cadastrar_produto(nome_loja:str,nome: str,descricao: str,preco: float,quantidade_em_estoque: int,categoria: str,imagens: List[str]):
    for loja in lojas:
        if loja.nome == nome_loja:

            novo_produto = Produto(
                id=len(loja.produtos) + 1,
                nome=nome,
                descricao=descricao,
                preco=preco,
                quantidade_em_estoque=quantidade_em_estoque,
                categoria=categoria,
                imagens=imagens)
            
            loja.produtos.append(novo_produto)
            return novo_produto 

# deletar produto
@app.delete("/produtos/{nome}", response_model=Produto)
def excluir_produto(loja_nome:str,nome: str):
    for loja in lojas:
        if loja.nome == loja_nome:

            for num, produto in enumerate(loja.produtos):
                if produto.nome == nome:
                    loja.produtos.pop(num)

                    # Atualiza IDs
                    for n, prod in enumerate(loja.produtos):
                        prod.id = n + 1
                        

                    return produto

    raise HTTPException(404, "Produto não encontrado")
    

# buscar pedidos
@app.get("/pedidos", response_model=List[Pedido])
def listar_pedidos(nome_loja:str):
    for loja in lojas:
        if loja.nome == nome_loja:
            return loja.pedidos
    raise HTTPException(404,"Não localizado.")

# buscar pedido
@app.get("/pedidos/{nome}", response_model=Pedido)
def buscar_pedido(nome_loja:str,id_pedido: int):
    for loja in lojas:
        if loja.nome == nome_loja:
            for pedido in loja.pedidos:
                if pedido.id == id_pedido:
                    return pedido
    raise HTTPException(404, "Pedido não encontrado")

#cadastrar pedido
@app.post("/pedidos", response_model=Pedido)
def cadastrar_pedido(nome_loja:str, lista_id_produtos: List[int], status: str, endereco_entrega:str, forma_pagamento:str):
    for loja in lojas:
        if loja.nome == nome_loja:
            lista_produtos = []
            for prod in loja.produtos:
                if prod.id in lista_id_produtos:
                    lista_produtos.append(prod)

            novo_pedido = Pedido(
                id=len(loja.pedidos) + 1,
                usuario=user_logado,
                produtos = lista_produtos,
                data_pedido=datetime.datetime.now().date(),
                status= status,
                endereco_entrega=endereco_entrega,
                forma_pagamento=forma_pagamento)
            
            loja.pedidos.append(novo_pedido)
            return novo_pedido
    
# apagar pedido
@app.delete("/pedido/{nome}", response_model=Pedido)
def excluir_pedido(loja_nome:str,id_pedido: int):
    for loja in lojas:
        if loja.nome == loja_nome:

            for num, pedido in enumerate(loja.pedidos):
                if pedido.id == id_pedido:
                    loja.pedidos.pop(num)

                    # Atualiza IDs
                    for n, ped in enumerate(loja.pedidos):
                        ped.id = n + 1

                    return pedido

    raise HTTPException(404, "pedido não encontrado")

# buscar avaliação
@app.get("/avaliacoes", response_model=List[Avaliacao])
def listar_avaliacoes(nome_loja:str):
    for loja in lojas:
        if loja.nome == nome_loja:
            return loja.avaliacoes
    raise HTTPException(404,"Não localizado.")

# buscar avaliação
@app.get("/avaliacoes/{nome}", response_model=Avaliacao)
def buscar_avaliacao(nome_loja:str,id_avali: int):
    for loja in lojas:
        if loja.nome == nome_loja:
            for avaliacao in loja.avaliacoes:
                if avaliacao.id == id_avali:
                    return avaliacao
    raise HTTPException(404, "avaliacao não encontrado")

#cadastrar avaliação
@app.post("/avaliacoes", response_model=Avaliacao)
def cadastrar_avaliacao(nome_loja:str, produto_id:int, nota:int, comentario:str):
    for loja in lojas:
        if loja.nome == nome_loja:

            for prod in loja.produtos:
                if prod.id == produto_id:
                    produto_avali = prod
            
            #ajeitar o usuario da valiação 
            # bug = quando muda de usuario o user cadastrado na avaliação muda para o logado atual (usuario = user_logado)
            nova_avaliacao = Avaliacao(
                id=len(loja.avaliacoes) + 1,
                usuario=user_logado,
                produto = produto_avali,
                nota=nota,
                comentario = comentario,
                data_avaliacao=datetime.datetime.now().date()
                )
            
            loja.avaliacoes.append(nova_avaliacao)
            return nova_avaliacao
        
# apagar avaiação
@app.delete("/avaliacoes/{nome}", response_model=Avaliacao)
def excluir_avaliacao(loja_nome:str,id_avaliacao: int):
    for loja in lojas:
        if loja.nome == loja_nome:

            for num, avaliacao in enumerate(loja.avaliacoes):
                if avaliacao.id == id_avaliacao:
                    loja.avaliacoes.pop(num)

                    # Atualiza IDs
                    for n, avali in enumerate(loja.avaliacoes):
                        avali.id = n + 1

                    return avaliacao

    raise HTTPException(404, "avaliação não encontrado")
   
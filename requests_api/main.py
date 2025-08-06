import requests # pip install requests
import time
from colorama import Fore # pip install colorama

def cadastrar(name, email, senha):
    user = {"username": name, "password": senha, "email": email}
    response = requests.post("http://127.0.0.1:8000/usuarios", json=user)

    if response.status_code == 200:
        msg = Fore.GREEN +f"({email}) cadastrado com sucesso!"+Fore.WHITE
        return msg
    else:
        msg = Fore.RED +f"Não foi possível cadastrar, tente novamente!"+Fore.WHITE
        return msg
    
def apagar_cadastro(username):
    request = requests.delete(f'http://127.0.0.1:8000/usuarios/{username}')
    
    if request.status_code == 200:
        return Fore.GREEN +"Usuario apagado com sucesso!"+Fore.WHITE
    else:
        return Fore.RED +"Não foi possível apagar o usuario!"+Fore.WHITE
    

    
def logar(email, senha):
    user = {"email":email, "password":senha}
    login=requests.post(f'http://127.0.0.1:8000/login',params=user)

    if login.status_code == 200:
        msg = Fore.GREEN +f"{email} logado com sucesso!"+Fore.WHITE
        return msg
    else:
        msg = Fore.RED +f"Não foi possível logar, tente novamente!"+Fore.WHITE
        return msg
    
def logout():
    request = requests.get("http://127.0.0.1:8000/logout")
    livros = request.json()

    if request.status_code == 200:
        return 'logout concluido'
    else: 
        return None
    

def add_loja(nome, descricao, logo):
    loja = {"nome":nome, "descricao":descricao, "logo":logo}
    add=requests.post(f'http://127.0.0.1:8000/lojas',params=loja)

    if add.status_code == 200:
        if add.text == 'Deslogado':
            return "É necessário fazer o login!"
        else:
            msg = Fore.GREEN +f"{nome} adicionado com sucesso a lista de lojas!"+Fore.WHITE
            return msg
    else:
        msg = Fore.RED +f"Não foi possível adicionar {nome} a lista de lojas, tente novamente!"+Fore.WHITE
        return msg
    
    
def apagar_loja(nome):
    request = requests.delete(f'http://127.0.0.1:8000/lojas/{nome}')
    
    if request.status_code == 200:
        return Fore.GREEN +"Loja apagada com sucesso!"+Fore.WHITE
    else:
        return Fore.RED +"Não foi possível apagar a loja!"+Fore.WHITE
    

def listar_lojas():
    request = requests.get("http://127.0.0.1:8000/lojas")
    print(request.text)
    lojas = request.json()

    if request.status_code == 200:
        return lojas
    else: 
        return None
    

def buscar_loja(nome):
    request = requests.get(f'http://127.0.0.1:8000/lojas/{nome}')
    loja = request.json()

    if request.status_code == 200:
        return loja
    else:
        return None
    



def add_produto(nome, descricao, preco, quantidade_em_estoque,categoria, imagens):
    produto = {"nome":nome, "descricao":descricao, "preco":preco, "quantidade_em_estoque":quantidade_em_estoque, "categoria":categoria, "imagens":imagens}
    add=requests.post(f'http://127.0.0.1:8000/produtos',json=produto)

    if add.status_code == 200:
        msg = Fore.GREEN +f"{nome} adicionado com sucesso a lista de produtos!"+Fore.WHITE
        return msg
    else:
        msg = Fore.RED +f"Não foi possível adicionar {nome} a lista de produtos, tente novamente!"+Fore.WHITE
        return msg
    
    
def apagar_produto(nome):
    request = requests.delete(f'http://127.0.0.1:8000/produtos/{nome}')
    
    if request.status_code == 200:
        return Fore.GREEN +"Produto apagado com sucesso!"+Fore.WHITE
    else:
        return Fore.RED +"Não foi possível apagar o produto!"+Fore.WHITE
    

def listar_produtos():
    request = requests.get("http://127.0.0.1:8000/produtos")
    print(request.text)
    produtos = request.json()

    if request.status_code == 200:
        return produtos
    else: 
        return None
    

def buscar_produto(nome):
    request = requests.get(f'http://127.0.0.1:8000/produtos/{nome}')
    produto = request.json()

    if request.status_code == 200:
        return produto
    else:
        return None
    


    
def add_pedido(nome, descricao, preco, quantidade_em_estoque,categoria, imagens):
    pedido = {"nome":nome, "descricao":descricao, "preco":preco, "quantidade_em_estoque":quantidade_em_estoque, "categoria":categoria, "imagens":imagens}
    add=requests.post(f'http://127.0.0.1:8000/pedidos',json=pedido)

    if add.status_code == 200:
        msg = Fore.GREEN +f"Pedido adicionado com sucesso a lista de pedidos!"+Fore.WHITE
        return msg
    else:
        msg = Fore.RED +f"Não foi possível dicionar o pedido, tente novamente!"+Fore.WHITE
        return msg
    
    
def apagar_pedido(id_pedido):
    request = requests.delete(f'http://127.0.0.1:8000/pedidos/{id_pedido}')
    
    if request.status_code == 200:
        return Fore.GREEN +"Pedido apagado com sucesso!"+Fore.WHITE
    else:
        return Fore.RED +"Não foi possível apagar o pedido!"+Fore.WHITE
    

def listar_pedidos():
    request = requests.get("http://127.0.0.1:8000/pedidos")
    print(request.text)
    pedidos = request.json()

    if request.status_code == 200:
        return pedidos
    else: 
        return None
    

def buscar_pedido(id_pedido):
    request = requests.get(f'http://127.0.0.1:8000/pedidos/{id_pedido}')
    pedido = request.json()

    if request.status_code == 200:
        return pedido
    else:
        return None





def add_avaliacao(nome, descricao, preco, quantidade_em_estoque,categoria, imagens):
    avaliacao = {"nome":nome, "descricao":descricao, "preco":preco, "quantidade_em_estoque":quantidade_em_estoque, "categoria":categoria, "imagens":imagens}
    add=requests.post(f'http://127.0.0.1:8000/avaliacoes',json=avaliacao)

    if add.status_code == 200:
        msg = Fore.GREEN +f"{nome} adicionado com sucesso a lista de produtos!"+Fore.WHITE
        return msg
    else:
        msg = Fore.RED +f"Não foi possível adicionar a avaliação a lista de produtos, tente novamente!"+Fore.WHITE
        return msg
    
    
def apagar_avaliacao(nome):
    request = requests.delete(f'http://127.0.0.1:8000/avaliacoes/{nome}')
    
    if request.status_code == 200:
        return Fore.GREEN +"Avaliação apagada com sucesso!"+Fore.WHITE
    else:
        return Fore.RED +"Não foi possível apagar a avaliação!"+Fore.WHITE
    

def listar_avaliacoes():
    request = requests.get("http://127.0.0.1:8000/avaliacoes")
    print(request.text)
    avaliacoes = request.json()

    if request.status_code == 200:
        return avaliacoes
    else: 
        return None
    

def buscar_avaliacao(nome):
    request = requests.get(f'http://127.0.0.1:8000/avaliacoes/{nome}')
    avaliacao = request.json()

    if request.status_code == 200:
        return avaliacao
    else:
        return None





if __name__ == "__main__":
    while True:
        print()
        print(("-"*10)+Fore.LIGHTCYAN_EX+" Bem Vindo ao GestorTech "+Fore.WHITE+("-"*10))
        print(" [0] - Sair")
        print(" [1] Login ou [2] Logout")
        print(" [3] Fazer Cadastro")
        print(" [4] Apagar Cadastro")
        print('')
        print(" [5] - Cadastrar Loja")
        print(" [6] - Deletar Loja")
        print(" [7] - Listar Lojas")
        print(" [8] - Buscar Loja")
        print('')
        print(" [9] - Cadastrar Produto")
        print(" [10] - Deletar Produto")
        print(" [11] - Listar Produtos")
        print(" [12] - Buscar Produto")
        print('')
        print(" [13] - Cadastrar Pedido")
        print(" [14] - Deletar Pedido")
        print(" [15] - Listar Pedidos")
        print(" [16] - Buscar Pedido")
        print('')
        print(" [17] - Cadastrar Avaliação")
        print(" [18] - Deletar Avaliação")
        print(" [19] - Listar Avaliações")
        print(" [20] - Buscar Avaliação")
        print('')


        print("-"*29)
        comando = int(input(Fore.LIGHTYELLOW_EX +"- Escolha uma opção: "+Fore.WHITE))

        if comando == 0:
            print(Fore.LIGHTRED_EX+"Saindo", end='')
            for i in range(3):
                print(".", end='', flush=True)  
                time.sleep(0.5)
            print(Fore.WHITE)
            break


        if comando == 1:

            print("-="*2+" L O G I N "+"-="*2)
            email = str(input(' - Email: '))
            senha = int (input(' - Senha: '))
        
            login = logar(email=email, senha=senha)

            print("-"*30)
            print(login)

        if comando == 2:
            logout = logout()

            if logout:
                print("-> Logout concluido!")
            else:
                print('-> Não possível fazer o logout')
            time.sleep(1)


        if comando == 3:
            print("-"*30)
            print("     Fazer Cadastro  ")
            name = str(input('- Username: '))
            email = str(input('- Email: '))
            senha = str(input('- Senha: '))
        
            cadastro = cadastrar(name=name, email=email, senha=senha)
            print("-"*30)
            print(cadastro)

        if comando == 4:
            print("-="*4+" APAGAR CADASTRO "+"-="*4)
            username = str(input(' - Digite o nome do usuario: '))
            status = apagar_cadastro(username)
            
            print(Fore.LIGHTBLACK_EX+"Apagando", end='')
            for i in range(2):
                print(".", end='', flush=True) 
                time.sleep(0.5)
            print()
            print(Fore.WHITE)
            print("-="*15)
            print(status)

        if comando == 5:

            print("-="*2+" CADASTRAR lOJA "+"-="*2)
            nome = str(input(' - Nome: '))
            descricao = str(input(' - Descrição: '))
            logo = str(input('Logo: (baixar foto)'))

            add_loja = add_loja(nome=nome, descricao=descricao, logo=logo)

            print("-"*30)
            print(add_loja)

        if comando == 6:
            print("-="*4+" APAGAR LOJA "+"-="*4)
            nome = str(input(' - Digite o nome da loja: '))
            status = apagar_loja(nome)
            
            print(Fore.LIGHTBLACK_EX+"Apagando", end='')
            for i in range(2):
                print(".", end='', flush=True) 
                time.sleep(0.5)
            print()
            print(Fore.WHITE)
            print("-="*15)
            print(status)

        if comando == 7:
            print("-="*4+" LISTAR LOJAS "+"-="*4)
            listar_lojas = listar_lojas()

            for n,loja in enumerate(listar_lojas):
                print("-="*15)
                print(" "*12+f"Loja {n+1}")
                print(f" - Nome: {loja['nome']}")
        time.sleep(2)

        if comando == 8:
            print("-"*30)
            print()
            print("-"*10+" BUSCAR LOJA "+"-"*10)
            nome = str(input(f"- Digite o nome da loja: "))
            loja = buscar_loja(nome)
            print()
            print(Fore.LIGHTBLACK_EX+"Buscando", end='')
            for i in range(2):
                print(".", end='', flush=True) 
                time.sleep(0.5)
            print()
            print(Fore.WHITE)

            if loja:
                print("-"*30)
                print(" "*10+f"Loja Encontrada")
                print("-"*30)
                print(f" Nome: {loja['nome']}")
                print(f" Descrição: {loja['descricao']}")
              


        if comando == 9:

            print("-="*2+" CADASTRAR PRODUTO "+"-="*2)
            nome_loja = str(input(' - Nome da loja: '))
            nome = str(input(' - Nome do produto: '))
            descricao = str(input('Descrição: '))
            preco = float(input('Preço: '))
            quant_estoque = int(input('Estoque: '))
            categoria = str(input('Categoria: '))
            imagens = str(input('Imagens: '))
            
            add_produto = add_produto(nome=nome, descricao=descricao, preco=preco, quantidade_em_estoque=quant_estoque, categoria=categoria, imagens=imagens)

            print("-"*30)
            print(add_produto)

        if comando == 10:
            print("-="*4+" APAGAR PRODUTO "+"-="*4)
            nome = str(input(' - Digite o nome do produto: '))
            status = apagar_produto(nome)
            
            print(Fore.LIGHTBLACK_EX+"Apagando", end='')
            for i in range(2):
                print(".", end='', flush=True) 
                time.sleep(0.5)
            print()
            print(Fore.WHITE)
            print("-="*15)
            print(status)

        if comando == 11:
            print("-="*4+" LISTAR PRODUTOS "+"-="*4)
            listar_produtos = listar_produtos()

            for n,prod in enumerate(listar_produtos):
                print("-="*15)
                print(" "*12+f"Produto {n+1}")
                print(f" - Nome: {prod['nome']}")
                print(f" - Descrição: {prod['descricao']}")
                print(f" - Preço: {prod['preco']}")
                print(f" - Estoque: {prod['quantidade_em_estoque']}")
                print(f" - Categoria: {prod['categoria']}")

            time.sleep(2)

        if comando == 12:
            print("-"*30)
            print()
            print("-"*10+" BUSCAR PRODUTO "+"-"*10)
            nome = str(input(f"- Digite o nome do produto: "))
            prod = buscar_produto(nome)
            print()
            print(Fore.LIGHTBLACK_EX+"Buscando", end='')
            for i in range(2):
                print(".", end='', flush=True) 
                time.sleep(0.5)
            print()
            print(Fore.WHITE)

            if prod:
                print("-"*30)
                print(" "*10+f"Produto Encontrado")
                print("-"*30)
                print(f" - Nome: {prod['nome']}")
                print(f" - Descrição: {prod['descricao']}")
                print(f" - Preço: {prod['preco']}")
                print(f" - Estoque: {prod['quantidade_em_estoque']}")
                print(f" - Categoria: {prod['categoria']}")
        
            time.sleep(1)
        
        
        
        if comando == 13:
            list_prod = []
            print("-="*2+" CADASTRAR PEDIDO "+"-="*2)
            nome_loja = str(input(' - Nome da loja: '))
            cont = int(input('Quantos produtos? '))

            for i in range(0,cont):
                prod = int(input(f'Id do {i}° produto: '))
                list_prod.append(prod)

            status = str(input('Status: '))
            endereco_entrega = str(input('Endereço: '))
            forma_pagamento = str(input('FOrma de pagamento: '))
            
            add_pedido = add_pedido(nome_loja=nome_loja, lista_id_produtos=list_prod, status=status, endereco_entrega=endereco_entrega, forma_pagamento=forma_pagamento)

            print("-"*30)
            print(add_pedido)

        if comando == 14:
            print("-="*4+" APAGAR PEDIDO "+"-="*4)
            id = str(input(' - Digite o ID do pedido: '))
            status = apagar_pedido(id)
            
            print(Fore.LIGHTBLACK_EX+"Apagando", end='')
            for i in range(2):
                print(".", end='', flush=True) 
                time.sleep(0.5)
            print()
            print(Fore.WHITE)
            print("-="*15)
            print(status)

        if comando == 15:
            print("-="*4+" LISTAR PEDIDOS "+"-="*4)
            listar_pedidos = listar_pedidos()

            for n,ped in enumerate(listar_pedidos):
                print("-="*15)
                print(" "*12+f"Pedido {n+1}")
                print(f" - Cliente: {ped['usuario']}")
                print(f" - Produtos: {ped['produtos']}")
                print(f" - Data Pedido: {ped['data_pedido']}")
                print(f" - Status: {ped['status']}")

            time.sleep(2)

        if comando == 16:
            print("-"*30)
            print()
            print("-"*10+" BUSCAR PEDIDO "+"-"*10)
            id_pedido = str(input(f"- Digite o id do pedido: "))
            ped = buscar_pedido(id_pedido)
            print()
            print(Fore.LIGHTBLACK_EX+"Buscando", end='')
            for i in range(2):
                print(".", end='', flush=True) 
                time.sleep(0.5)
            print()
            print(Fore.WHITE)

            if prod:
                print("-="*15)
                print(" "*12+f"Pedido Encontrado {n+1}")
                print(f" - Cliente: {ped['usuario']}")
                print(f" - Produtos: {ped['produtos']}")
                print(f" - Data Pedido: {ped['data_pedido']}")
                print(f" - Status: {ped['status']}")
            time.sleep(1)
        
        
        
        if comando == 17:
            list_prod = []
            print("-="*2+" CADASTRAR AVALIAÇÃO "+"-="*2)
            nome_loja = str(input(' - Nome da loja: '))
            id_prod = int(input('ID do produto: '))
            nota = int(input('Nota do produto: '))
            comentario = str(input('Comentário: '))

            add_avali = add_avaliacao(nome_loja=nome_loja, id_produto=id_prod, status=status, endereco_entrega=endereco_entrega, forma_pagamento=forma_pagamento)

            print("-"*30)
            print(add_avali)

        if comando == 18:
            print("-="*4+" APAGAR AVALIAÇÃO "+"-="*4)
            id = str(input(' - Digite o ID da avaliação: '))
            status = apagar_avaliacao(id)
            
            print(Fore.LIGHTBLACK_EX+"Apagando", end='')
            for i in range(2):
                print(".", end='', flush=True) 
                time.sleep(0.5)
            print()
            print(Fore.WHITE)
            print("-="*15)
            print(status)

        if comando == 19:
            print("-="*4+" LISTAR AVALIAÇÕES "+"-="*4)
            listar_avali = listar_avaliacoes()

            for n,avali in enumerate(listar_avali):
                print("-="*15)
                print(" "*12+f"Avliação {n+1}")
                print(f" - Cliente: {avali['usuario']}")
                print(f" - Produto: {avali['produto']}")
                print(f" - Data avaliação: {avali['data_avaliacao']}")
                print(f" - Comentario: {avali['comentario']}")

            time.sleep(2)

        if comando == 20:
            print("-"*30)
            print()
            print("-"*10+" BUSCAR AVALIAÇÃO "+"-"*10)
            id_avali = str(input(f"- Digite o id da avaliação: "))
            avali = buscar_avaliacao(id_avali)
            print()
            print(Fore.LIGHTBLACK_EX+"Buscando", end='')
            for i in range(2):
                print(".", end='', flush=True) 
                time.sleep(0.5)
            print()
            print(Fore.WHITE)

            if avali:
                print("-="*15)
                print(" "*12+f"Avaliação Encontrada {n+1}")
                print(f" - Cliente: {avali['usuario']}")
                print(f" - Produtos: {avali['produtos']}")
                print(f" - Data avaliacao: {avali['data_avaliacao']}")
                print(f" - Status: {avali['status']}")
            time.sleep(1)
        

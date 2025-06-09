# Documentação do Projeto

## 1. Visão Geral

### Tecnologia Utilizada:
- Python
- FastAPI
- Uvicorn
- React
- JSON

### Descrição:
Plataforma multiloja de e-commerce de eletrônicos, onde diferentes lojistas podem cadastrar e gerenciar suas próprias lojas. O usuário final pode selecionar uma loja específica para visualizar e comprar seus produtos.

### Objetivo:
Oferecer uma plataforma moderna, escalável e organizada para que várias lojas de eletrônicos operem em um único ambiente, com uma experiência de compra personalizada e separada por loja.

## 2. Descrição Detalhada do Projeto

### O que é o projeto?
Uma rede de lojas de eletrônicos em um único site, permitindo que cada lojista tenha seu espaço próprio (com catálogo, estoque e pedidos), enquanto o usuário final pode navegar entre lojas e efetuar compras, filtrando por categorias, preços e avaliações, garantindo controle e logística mais simples para cada vendedor.

### 2.1 Funcionalidades Principais

#### Funcionalidade 01: Seleção e Navegação por Loja
- Página inicial com destaques e lojas em destaque
- Filtros por avaliação
- Acesso ao catálogo de uma loja específica
- Página de detalhes com especificações, imagens e avaliações

#### Funcionalidade 02: Painel do Lojista (Administrador de Loja)
- Cadastro de loja com informações e personalização
  - CRUD de produtos, upload de imagens e categorias
  - Controle de estoque e promoções
  - Acompanhamento de pedidos da própria loja
  - Relatórios por período, produto e cliente

#### Funcionalidade 03: Carrinho de Compras (Usuário)
- Adicionar produtos no carrinho de compra
  - Cadastro/login (com opção de Google)
  - Finalizar compra (com endereço caso seja para entrega e formas de pagamento)
  - Pedido gerado com confirmação por e-mail

#### Funcionalidade 04: Pós-venda
- “Meus Pedidos”
  - Avaliação do produto e da loja
  - Solicitação de devolução/troca por pedido individual

#### Funcionalidade 05: Funcionalidades Avançadas Globais
- Lista de desejos
- Cupons de desconto 
- Notificações por e-mail (compra, envio, etc.)

### 2.2 Arquitetura do Código
```
eletroshop_network/
├── main.py # Inicialização da aplicação FastAPI
├── api.py # Rotas da API
├── models.py # Modelos de dados (lojas, produtos, pedidos, usuários)
├── database.py # Conexão e sessão com o banco de dados
├── schemas/ # Schemas Pydantic para validações
├── auth/ # JWT, login com redes sociais, permissão por papel
├── admin/ # Painel de controle do lojista
├── static/ # Armazenamento de arquivos
├── templates/ # Componentes do design (HTML)
├── requirements.txt # Requisitos para instalação
└── docs.md # Documentação
```

## 3. Etapas de Entrega (Cronograma Detalhado)
- **Etapa 1:** 
- **Etapa 2:** 
- **Etapa 3:** 
- **Etapa 4:** 
- **Etapa 5:** 

# Documentação do Projeto: Projeto GestorTech

## 1. Visão Geral

### Tecnologia Utilizada:
- Python
- FastAPI
- Uvicorn
- React

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
GestorTech/
├── main.py # Inicialização da aplicação FastAPI
├── models.py # Modelos de dados (lojas, produtos, pedidos, usuários)
├── database.py # Conexão e sessão com o banco de dados
├── schemas/ # Schemas Pydantic para validações
├── static/ # Armazenamento de arquivos
├── templates/ # Componentes do design (HTML)
├── requirements.txt # Requisitos para instalação
└── docs.md # Documentação
```
## 3. Etapas de Entrega (Cronograma Detalhado)

### Etapa 1: Reunião Inicial e Levantamento de Requisitos
- Reunião de definição de escopo do projeto
- Levantamento dos requisitos funcionais e não funcionais
- Configurar repositório e ambiente de desenvolvimento
- Identificar papéis do sistema: usuário, lojista, administrador

### Etapa 2: Elaboração de Diagramas
- Criar Diagrama de Casos de Uso 
- Criar Diagrama de Classes
- Criar Diagrama de Atividades

### Etapa 3: Definição da Arquitetura e Estrutura Inicial do Projeto
- Planejar e documentar a arquitetura geral:
  - Backend: FastAPI + Uvicorn 
  - Frontend: React
- Definir os diretórios principais do backend (models.py, main.py, auth/, schemas/, etc.)
- Definir rotas básicas da API

### Etapa 4: Definição dos Models e Schemas
- Especificar os modelos de dados (loja, produto, usuário, pedido, avaliação, etc.)
- Esboçar os models.py com atributos e tipos
- Escrever os schemas Pydantic (entrada e saída de dados)

### Etapa 5: Planejamento das Funcionalidades e Endpoints
- Mapear funcionalidades por papel (cliente, lojista, admin)
- Especificar os métodos HTTP, parâmetros e respostas esperadas
- Listar todos os endpoints RESTful necessários:
  - Autenticação, cadastro de usuários
  - CRUD de loja e produto
  - Parâmetros e respostas esperadas
- Esboçar as principais telas e componentes React


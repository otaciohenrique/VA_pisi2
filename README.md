# VA_PISI - Sistema de Gestão de Coquetéis

## O Projeto consiste em um sistema interativo via CLI (Command Line Interface) voltado para a gestão técnica e operacional de Drinks e Coquetéis. Ele foi desenhado para facilitar o controle de receitas, ingredientes e autenticação de usuários, cruzando dados de estoque em tempo real.

# 🚀 Funcionalidade de Inovação: Estoque Inteligente (Cardápio Dinâmico)
**O grande diferencial técnico deste projeto é o algoritmo de Estoque Inteligente. Diferente de um cardápio estático comum, o sistema realiza um cruzamento de dados  em tempo real entre os ingredientes necessários para cada receita (em cardapio.py) e os itens marcados como disponíveis (em estoque.py).**
**Resultado: O usuário só visualiza no painel do cardápio os drinks que realmente podem ser preparados com o estoque atual, otimizando a operação do bar e evitando pedidos impossíveis de serem atendidos.**

# 🛠️ Tecnologias e Bibliotecas Utilizadas
##  O projeto foi desenvolvido em Python e utiliza as seguintes bibliotecas:**
**Bibliotecas Externas (Requerem instalação)**
- **rich:** Biblioteca principal para a construção da interface de usuário no terminal. Substitui os prints convencionais por uma interface visualmente agradável, utilizando módulos como Console, Panel, Table e box. Ela permite estilizar textos, formatar tabelas de exibição de dados (como o estoque e menus) e criar painéis modulares, aproximando a experiência CLI de uma GUI de forma leve.
**Bibliotecas Nativas (Built-in)**
- **os:** Utilizada para executar comandos do sistema operacional (ex: os.system('cls')), garantindo que o terminal seja limpo a cada transição de tela, mantendo a interface fluida e sem poluição visual.
- **datetime:** Aplicada no módulo de cadastro de usuários (cadastro.py) para capturar a data atual e calcular, com precisão, a idade do usuário a partir da string de data de nascimento, implementando uma trava de segurança (proibido para menores de 18 anos).

# 📂 Organização dos Módulos e Arquitetura
**O código reflete uma arquitetura modularizada, separando responsabilidades para facilitar a manutenção e escalabilidade do sistema:**
- **main.py:**  Ponto de entrada (entry point) da aplicação. Responsável apenas por invocar o loop principal.
- **usuario/:** (Módulo de Autenticação e Perfis):
    - **menu_iniciar.py:** Roteador inicial de navegação (Login/Cadastro).
    - **login.py:** Lógica de validação de credenciais de acesso.
    - **cadastro.py:** Lida com regras de negócio para a criação de usuários (validação de idade mínima, força de senha e unicidade de nome).
    - **usuarios.py:** Base de dados (estruturas de dados em memória) dos usuários. 
- **sistema/:**  (Módulo de Regras de Negócio do Bar):
    - **menu_usuario.py:** Dashboard principal logado, conectando as funcionalidades do sistema.
    - **cardapio.py:** CRUD completo de drinks e a lógica do cruzamento de dados com o estoque.
    - **estoque.py:** Gerenciamento do estado (Disponível/Indisponível) de cada ingrediente.
    - **utils.py:** Funções utilitárias e reaproveitáveis, como a sanitização de strings (limpar_texto) para buscas robustas (case-insensitive e ignorando acentos).

# ⚙️ Como Rodar o Projeto
## 1. Pré-requisitos
**Certifique-se de ter o Python 3.x instalado em sua máquina.**

## 2. Instalação das Dependências
**Para que a interface gráfica via terminal funcione corretamente, instale a biblioteca rich utilizando o gerenciador de pacotes do Python:**
pip install rich

## 3. Execução
**No terminal, navegue até a raiz do projeto (onde está localizado o arquivo main.py) e execute o comando:**
python main.py

# 🗺️ Funcionalidades
## release 1.0
- **Catálogo Centralizado:** Visualização de todos os drinks e fichas técnicas em ordem alfabética.
- **Sistema de Busca Inteligente:** Encontra coquetéis pelo nome ou pesquisando por ingredientes específicos.
- **Gestão de Coquetéis:** Adição, edição e exclusão de drinks.
- **Gestão de Usuários:** Sistema completo para criar, visualizar, editar e remover o perfis de usuário logado.
  
## release 2.0
- **Gestão de Ingredientes** Adição, edição e exclusão de ingredientes e sua disponibilidade no estoque.
- **Estoque Inteligente:** Cruzamento de dados entre os ingredientes necessários e os ingredientes disponíveis.
- **Interface:** Utilização da biblioteca rich para a criação de uma interface agradável e intuitiva. 

# 1. Cardádio
# 2. Pesquisar
# 3. Gerenciador
    #1. Exibir Drinks
        #1. Criar Novo drink
        #2. Editar Drink
            #1. Editar Nome
            #2. Editar Ingredientes
            #3. Voltar
    #2. Exibir Ingredientes
        #1. Criar Novo Ingrediente
        #2. Editar Ingrediente
            #1. Editar Nome
            #2. Editar Disponibilidade
            #3. Voltar
# 4. Configurações
    # 1. Editar Nome de Usuário
    # 2. Editar Senha
    # 3. Voltar
# 5. Sair

def limpar_texto(texto):
    texto = texto.lower().strip()
    
    acentos = "áàãâéêíóõôúç"
    sem_acentos = "aaaaeeiooouc"
    
    for i in range(len(acentos)):
        texto = texto.replace(acentos[i], sem_acentos[i])
        
    return texto

 
def exibir_lista(lista_drinks, titulo="Cardápio"):
    print(f"\n--- {titulo.upper()} ---")
    if len(lista_drinks) == 0:
        print("Nenhum drink encontrado.")
    else:
        lista_ordenada = sorted(lista_drinks, key=lambda d: d["nome"])

        for i, drink in enumerate(lista_ordenada, 1):
            ingredientes_texto = ", ".join(drink["ingredientes"])
            print(f"{i}. {drink['nome']}")
            print(f"   Ingredientes: {ingredientes_texto}")
    print("-" * 30)




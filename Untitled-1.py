
# Cardápio 

cardapio = [
    {"nome": "Mojito", "ingredientes": ["Rum", "Hortelã", "Açúcar", "Suco de Limão", "Água com gás"]},
    {"nome": "Caipirinha", "ingredientes": ["Cachaça", "Limão", "Açúcar", "Gelo"]},
    {"nome": "Gin Tônica", "ingredientes": ["Gin", "Água Tônica", "Limão", "Gelo"]},
    {"nome": "Negroni", "ingredientes": ["Gin", "Campari", "Vermute Tinto", "Casca de Laranja", "Gelo"]},
    {"nome": "Margarita", "ingredientes": ["Tequila", "Licor de Laranja", "Suco de Limão", "Sal", "Gelo"]},
    {"nome": "Moscow Mule", "ingredientes": ["Vodka", "Cerveja ou Refrigerante de Gengibre", "Suco de Limão", "Xarope de Açúcar", "Gelo"]},
    {"nome": "Aperol Spritz", "ingredientes": ["Aperol", "Espumante Prosecco", "Água com gás", "Fatia de Laranja", "Gelo"]},
    {"nome": "Piña Colada", "ingredientes": ["Rum Branco", "Leite de Coco", "Suco de Abacaxi", "Gelo"]},
    {"nome": "Dry Martini", "ingredientes": ["Gin", "Vermute Seco", "Azeitona", "Gelo"]}
]


# BUSCA 
def limpar_texto(texto):
    # Passa tudo para minúsculo e tira os espaços das pontas
    texto = texto.lower().strip()
    
    # Substitui manualmente os caracteres com acento pelos sem acento
    acentos = "áàãâéêíóõôúç"
    sem_acentos = "aaaaeeiooouc"
    
    for i in range(len(acentos)):
        texto = texto.replace(acentos[i], sem_acentos[i])
        
    return texto

def buscar_drink(termo):
    resultados = []
    termo_limpo = limpar_texto(termo)
    
    for drink in cardapio:
        nome_limpo = limpar_texto(drink["nome"])
        
        if termo_limpo in nome_limpo:
            resultados.append(drink)
            continue 
        
        for ingrediente in drink["ingredientes"]:
            ingrediente_limpo = limpar_texto(ingrediente)
            if termo_limpo in ingrediente_limpo:
                resultados.append(drink)
                break 
                
    return resultados

# EXIBIÇÃO 
def exibir_lista(lista_drinks, titulo="Cardápio"):
    print(f"\n--- {titulo.upper()} ---")
    if len(lista_drinks) == 0:
        print("Nenhum drink encontrado.")
    else:
        for i, drink in enumerate(lista_drinks, 1):
            ingredientes_texto = ", ".join(drink["ingredientes"])
            print(f"{i}. {drink['nome']}")
            print(f"   Ingredientes: {ingredientes_texto}")
    print("-" * 30)


# MENU 
def iniciar_sistema():
    while True:
        print("\n" + "="*30)
        print(" cATÁLOGO DE COQUETÉIS")
        print("="*30)
        print("1. Mostrar Todos os Drinks")
        print("2. Buscar Drink ou Ingrediente")
        print("3. Adicionar Novo Drink")
        print("4. Deletar um Drink")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção (1-5): ").strip()
        
        # OPÇÃO 1
        if opcao == "1":
            exibir_lista(cardapio, "Cardápio Completo")
            
        # OPÇÃO 2
        elif opcao == "2":
            termo = input("\nDigite o nome ou ingrediente para buscar: ")
            resultados = buscar_drink(termo)
            exibir_lista(resultados, f"Resultados para '{termo}'")
            
        # OPÇÃO 3
        elif opcao == "3":
            print("\n--- Adicionar Novo Drink ---")
            nome = input("Nome do drink: ").strip()
            ingredientes_texto = input("Ingredientes: ").strip()
            
            if nome == "" or ingredientes_texto == "":
                print("⚠️ Erro: Nome e ingredientes não podem ficar em branco.")
            else:
                lista_ingredientes = [ingrediente.strip() for ingrediente in ingredientes_texto.split(",")]
                novo_drink = {"nome": nome, "ingredientes": lista_ingredientes}
                cardapio.append(novo_drink)
                print(f"✅ Drink '{nome}' adicionado com sucesso!")
                
        # OPÇÃO 4
        elif opcao == "4":
            print("\n--- Deletar Drink ---")
            exibir_lista(cardapio, "Drinks Disponíveis")
            nome_deletar = input("\nDigite o NOME EXATO do drink que deseja deletar: ").strip()
            
            drink_encontrado = False
            for drink in cardapio:
                if limpar_texto(drink["nome"]) == limpar_texto(nome_deletar):
                    cardapio.remove(drink)
                    print(f"🗑 Drink '{drink['nome']}' deletado com sucesso!")
                    drink_encontrado = True
                    break 
            
            if not drink_encontrado:
                print(f"⚠️ Erro: Drink '{nome_deletar}' não encontrado no cardápio.")
                
        # OPÇÃO 5
        elif opcao == "5":
            print("\nSaindo do sistema...")
            break
            
        # OPÇÃO INVÁLIDA
        else:
            print("\n⚠️ Opção inválida! Digite um número de 1 a 5.")


# EXECUÇÃO
if __name__ == "__main__":
    iniciar_sistema()
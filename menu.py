from cardapio import cardapio 
from comuns import limpar_texto, exibir_lista

# BUSCA 


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



# ADICIONAR
def adicionar_drink(lista_cardapio):
    print("\n--- Adicionar Novo Drink ---")
    nome = input("Nome do drink: ").strip()
    ingredientes_texto = input("Ingredientes: ").strip()
            
    if nome == "" or ingredientes_texto == "":
        print("⚠️ Erro: Nome e ingredientes não podem ficar em branco.")
    else:
        lista_ingredientes = [ingrediente.strip() for ingrediente in ingredientes_texto.split(",")]
        novo_drink = {"nome": nome, "ingredientes": lista_ingredientes}
        lista_cardapio.append(novo_drink)
        print(f"✅ Drink '{nome}' adicionado com sucesso!")

# EDITAR
def editar_drink(lista_cardapio):
    print("\n--- Editar Drink ---")
    exibir_lista(lista_cardapio, "Drinks Disponíveis")
    nome_editar = input("\nDigite o NOME EXATO do drink que deseja editar:").strip()

    drink_encontrado = False
    for drink in lista_cardapio:
        if limpar_texto(drink["nome"]) == limpar_texto(nome_editar):
            drink_encontrado = True
            print(f"\nEditando: {drink['nome']} ")

            novo_nome = input(f"Novo nome: ").strip()
            if novo_nome != "":
                drink["nome"] = novo_nome

                ingredientes_atuais = ", ".join(drink["ingredientes"])
                print(f"Ingredientes: {ingredientes_atuais}")
                novos_ingredientes = input("Novos ingredientes separados por vírgula: ").strip()
                    
                if novos_ingredientes != "":            
                    lista_ingredientes = [i.strip() for i in novos_ingredientes.split(",")]
                    drink["ingredientes"] = lista_ingredientes
                        
                print(f"✅ Drink '{drink['nome']}' atualizado com sucesso!")
                break 
            
        if not drink_encontrado:
            print(f"⚠️ Erro: Drink '{nome_editar}' não encontrado no cardápio.")
# DELETAR
def deletar_drink(lista_cardapio):
    print("\n--- Deletar Drink ---")
    exibir_lista(lista_cardapio, "Drinks Disponíveis")
    nome_deletar = input("\nDigite o NOME EXATO do drink que deseja deletar: ").strip()
                 
    drink_encontrado = False
    for drink in lista_cardapio:
        if limpar_texto(drink["nome"]) == limpar_texto(nome_deletar):
            lista_cardapio.remove(drink)
            print(f"🗑 Drink '{drink['nome']}' deletado com sucesso!")
            drink_encontrado = True
            break 
                 
    if not drink_encontrado:
        print(f"⚠️ Erro: Drink '{nome_deletar}' não encontrado no cardápio.")
     
# MENU 
def iniciar_sistema():
    while True:
        print("\n" + "="*30)
        print(" CATÁLOGO DE COQUETÉIS")
        print("="*30)
        print("1. Mostrar Todos os Drinks")
        print("2. Buscar Drink ou Ingrediente")
        print("3. Adicionar Novo Drink")
        print("4. Editar um Drink")
        print("5. Deletar um Drink")
        print("6. Sair")
        
        opcao = input("\nEscolha uma opção (1-6): ").strip()
        
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
            adicionar_drink(cardapio)

        #OPÇÃO 4
        elif opcao == "4":
            editar_drink(cardapio)    

        # OPÇÃO 5
        elif opcao == "5":
            deletar_drink(cardapio)

        # OPÇÃO 6
        elif opcao == "6":
            print("\nSaindo do sistema...")
            break
            
        # OPÇÃO INVÁLIDA
        else:
            print("\n⚠️ Opção inválida! Digite um número de 1 a 6.")


# EXECUÇÃO
if __name__ == "__main__":
    iniciar_sistema()
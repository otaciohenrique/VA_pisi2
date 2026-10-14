from utils import limpar_texto, exibir_lista

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
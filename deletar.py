from utils import limpar_texto, exibir_lista

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
     
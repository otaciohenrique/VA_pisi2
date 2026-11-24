from sistema.utils import limpar_texto
from sistema.estoque import ingredientes
from rich.console import Console

console = Console()


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


def exibir_lista(lista_drinks, titulo="Cardápio"):
    console.clear ()
    console.print(f"\n--- {titulo.upper()} ---", style="bold yellow")
    if len(lista_drinks) == 0:
        print("Nenhum drink encontrado.")
    else:
        lista_ordenada = sorted(lista_drinks, key=lambda d: d["nome"])

        for i, drink in enumerate(lista_ordenada, 1):
            ingredientes_texto = ", ".join(drink["ingredientes"])
            print(f"{i}. {drink['nome']}")
            print(f"   Ingredientes: {ingredientes_texto}")
    print("-" * 30)


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


def mostrar_cardapio():
    estoque_disponivel = [
        limpar_texto(item["nome"]) for item in ingredientes if item["disponivel"]
    ]

    console.clear()
    console.print("[bold blue]--- CARDÁPIO ---[/bold blue]\n")

    nenhum_drink_disponivel = True

    for drink in cardapio:
        pode_fazer = True

        for ingrediente in drink["ingredientes"]:
            if limpar_texto(ingrediente) not in estoque_disponivel:
                pode_fazer = False
                break

        if pode_fazer:
            nenhum_drink_disponivel = False
            lista_ingredientes = ", ".join(drink["ingredientes"])
            console.print(f"[bold cyan]{drink['nome']}[/bold cyan]: [white]{lista_ingredientes}[/white]")

    if nenhum_drink_disponivel:
        console.print("[bold red]Não há ingredientes suficientes para nenhum drink no momento.[/bold red]")
        
    print()

    
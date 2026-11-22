from rich.console import Console
from rich.table import Table
from rich import box

console = Console()


def mostrar_estoque():
    ingredientes = [
        {"nome": "Vodka", "disponivel": True},
        {"nome": "Rum", "disponivel": False},
        {"nome": "Limão", "disponivel": True},
        {"nome": "Hortelã", "disponivel": False},
        {"nome": "Açúcar", "disponivel": True}
    ]

    disponiveis = [item for item in ingredientes if item["disponivel"] == True]
    indisponiveis = [item for item in ingredientes if item["disponivel"] == False]

    disponiveis = sorted(disponiveis, key=lambda x: x["nome"])
    indisponiveis = sorted(indisponiveis, key=lambda x: x["nome"])

    console.clear()

    tabela = Table(
        title="ESTOQUE DE INGREDIENTES", 
        title_style="bold blue",
        box=box.ROUNDED,
        show_header=False
    )
    
    tabela.add_column("Itens")

    for item in disponiveis:
        linha = f"[white]{item['nome']}[/white] - [bold green]Disponível[/bold green]"
        tabela.add_row(linha)

    if disponiveis and indisponiveis:
        tabela.add_section()

    for item in indisponiveis:
        linha = f"[white]{item['nome']}[/white] - [bold red]Indisponível[/bold red]"
        tabela.add_row(linha)

    print()
    console.print(tabela)
    print()

def opcoes_estoque():
    print ("1. Adicionar Ingrediente")
    print ("2. Editar Ingrediente")
    print ("3. Voltar ao Gerenciador")


mostrar_estoque()
opcoes_estoque()
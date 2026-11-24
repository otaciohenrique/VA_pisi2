from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

ingredientes = [
        {"nome": "Vodka", "disponivel": True},
        {"nome": "Rum", "disponivel": False},
        {"nome": "Limão", "disponivel": True},
        {"nome": "Hortelã", "disponivel": False},
        {"nome": "Açúcar", "disponivel": True}
    ]

def mostrar_estoque():

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

    while True:

        mostrar_estoque()
            
        print ("1. Adicionar")
        print ("2. Editar")
        print ("3. Voltar")

        opcao = console.input("\nEscolha uma opção (1-3): ").strip()

        if opcao == "1":
            adicionar_ingrediente()

        elif opcao == "2":
            editar_ingrediente()

        elif  opcao == "3":
            break

        else:
            console.print ("Opção Inválida! Digite um número de 1 a 3")

def adicionar_ingrediente():

    while True:
        
        nome = console.input("[yellow]Digite o nome do novo ingrediente:[/yellow] ").strip()
        if not nome:
            console.print("[bold red]O nome não pode ficar vazio![/bold red]\n")
            return
    
        resposta = console.input("[yellow]O ingrediente está disponível agora? (S/N):[/yellow] ").strip().upper()
        if resposta == "S":
            esta_disponivel = True
        else:
            esta_disponivel = False

        ingredientes.append({
            "nome": nome.capitalize(),
            "disponivel": esta_disponivel
        })

        console.print(f"\n[bold green]✅ '{nome.capitalize()}' adicionado com sucesso![/bold green]\n")

        console.input("Digite qualquer tecla para voltar")
        break

def editar_ingrediente():

    while True:

        nome = console.input("[yellow]Digite o nome do Ingrediente que deseja editar ou 'cancelar' para voltar:[/yellow] ").strip()

        if nome.lower() == 'cancelar':
            break
          
        encontrado = False

        for item in ingredientes:
            if item["nome"].lower() == nome.lower():
                encontrado = True

            novo_nome = console.input(f"[yellow]Novo nome (deixe em branco para manter '{item['nome']}'):[/yellow] ").strip()
            if novo_nome:
                item["nome"] = novo_nome.capitalize()


    



opcoes_estoque()
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

ingredientes = [
        {"nome": "Vodka", "disponivel": True},
        {"nome": "Rum", "disponivel": False},
        {"nome": "Limão", "disponivel": True},
        {"nome": "Hortelã", "disponivel": False},
        {"nome": "Açúcar", "disponivel": True},
        {"nome": "Gelo", "disponivel": True},
        {"nome": "Cachaça", "disponivel": True},
        {"nome": "Gin", "disponivel": True},
        {"nome": "Vermute Tinto", "disponivel": True},
        {"nome": "Campari", "disponivel": True}
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
        
        nome = console.input("Digite o nome do novo ingrediente: ").strip()
        if not nome:
            console.print("[bold red]O nome não pode ficar vazio![/bold red]\n")
            return
    
        resposta = console.input("O ingrediente está disponível ? (S/N): ").strip().upper()
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

                console.print(f"\n[bold green]Ingrediente '{item['nome']}' encontrado![/bold green]")

                print("\nO que você deseja editar?")
                print("1. Nome")
                print("2. Disponibilidade")

                escolha = console.input("\nEscolha uma opção (1-2): ").strip()

                if escolha == "1":
                    novo_nome = console.input(f"Digite o futuro nome (Atual: '{item['nome']}'): ").strip()
                    if novo_nome:
                        item["nome"] = novo_nome.capitalize()
                        console.print("[bold green]✅ Nome atualizado com sucesso![/bold green]\n")
                    else:
                        console.print("[bold red]O nome não pode ficar vazio![/bold red]\n")
                        
                elif escolha == "2":
                    status_atual = "S" if item["disponivel"] else "N"
                    novo_status = console.input(f"O ingrediente está disponível agora? (Atual: {status_atual}) (S/N):[/yellow] ").strip().upper()
                    
                    if novo_status == "S":
                        item["disponivel"] = True
                        console.print("[bold green]✅ Disponibilidade atualizada com sucesso![/bold green]\n")
                    elif novo_status == "N":
                        item["disponivel"] = False
                        console.print("[bold green]✅ Disponibilidade atualizada com sucesso![/bold green]\n")
                    else:
                        console.print("[bold red]Opção inválida! Nenhuma alteração foi feita.[/bold red]\n")
                        
                else:
                    console.print("[bold red]Opção Inválida![/bold red]\n")

                return

        if not encontrado:
            console.print("[bold red]Ingrediente não encontrado! Tente novamente.[/bold red]\n")


    




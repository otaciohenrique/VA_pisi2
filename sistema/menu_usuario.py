from sistema.cardapio import cardapio, mostrar_cardapio, opcoes_drink, buscar_drink
from rich.console import Console
from rich.table import Table
from rich.panel import Panel 
from rich import box
from sistema.estoque import opcoes_estoque
from usuario.usuarios import configuracao
import os

console = Console()


# MENU 
def menu_usuario(usuario_logado):
    while True:
        os.system('cls')
        painel = Panel("[bold blue] MENU  [/]", border_style="blue", expand=False)
        console.print(painel)

        tabela = Table(
            show_header=False, 
            box=box.ROUNDED
            )

        tabela.add_column("Opção", justify="center", style="bold white", no_wrap=True)
        tabela.add_column("Ação", style="white")

        tabela.add_row("1.", "Cardápio")
        tabela.add_row("2.", "Buscar Drink ou Ingrediente")
        tabela.add_row("3.", "Gerenciador")
        tabela.add_row("4.", "Configuração")
        tabela.add_row("5.", "Sair")
        
        print()
        console.print(tabela)
        
        opcao = input("\nEscolha uma opção (1-5): ").strip()
                
        # OPÇÃO 1
        if opcao == "1":
            mostrar_cardapio()
            console.input("\n[yellow]Pressione ENTER para voltar ao menu...[/yellow]")          
            
        # OPÇÃO 2
        elif opcao == "2":
            termo = console.input("\n[blue]Digite o nome ou ingrediente para buscar:[/blue]")
            buscar_drink(termo, cardapio)
            console.input("\n[yellow]Pressione ENTER para voltar ao menu...[/yellow]")
             
        # OPÇÃO 3
        elif opcao == "3":
            menu_gerenciar ()

        #OPÇÃO 4
        elif opcao == "4":
            configuracao(usuario_logado)         

        # OPÇÃO 5
        elif opcao == "5":
            print("\nSaindo da Conta")
            break
            
        # OPÇÃO INVÁLIDA
        else:
            print("\n⚠️ Opção inválida! Digite um número de 1 a 5.")

def menu_gerenciar ():
    while True:
        os.system('cls')
        painel = Panel("[bold blue] GERENCIADOR [/]", border_style="blue", expand=False)
        console.print(painel)
                   
        tabela = Table(
        show_header=False, 
        box=box.ROUNDED
        )
       
        tabela.add_column("Opção", justify="center", style="bold white", no_wrap=True)
        tabela.add_column("Ação", style="white")
       
       
        tabela.add_row("1.", "Exibir Drinks")
        tabela.add_row("2.", "Exibir Ingredientes")
        tabela.add_row("3.", "Sair")
       
        print()
        console.print(tabela) 

        opcao = console.input("\nEscolha uma opção (1-3): ").strip()

        if opcao == "1":
            opcoes_drink()

        elif opcao == "2": 
            opcoes_estoque()

        elif opcao == "3":
            break

        else:
            console.print("Por favor, digite um número de 1 a 3")
            console.input("[gray]Pressione ENTER para continuar...[/gray]")


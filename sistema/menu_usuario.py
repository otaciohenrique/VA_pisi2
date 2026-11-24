from sistema.cardapio import cardapio 
from sistema.utils import exibir_lista
from sistema.buscar import buscar_drink
from sistema.cardapio import adicionar_drink
from sistema.cardapio import editar_drink
from sistema.cardapio import deletar_drink
from rich.console import Console
from rich.table import Table

console = Console()


# MENU 
def menu_usuario():
    while True:
        console.clear
        tabela = Table(title="GERENCIADOR", title_style="bold blue")

        tabela.add_column("Opção", justify="center", style="bold white", no_wrap=True)
        tabela.add_column("Ação", style="white")

        tabela.add_row("1.", "Mostrar Todos os Drinks")
        tabela.add_row("2.", "Buscar Drink ou Ingrediente")
        tabela.add_row("3.", "Adicionar Drink")
        tabela.add_row("4.", "Editar um Drink")
        tabela.add_row("5.", "Deletar um Drink")
        tabela.add_row("6.", "Sair")

        print()
        console.print(tabela)
        
        opcao = input("\nEscolha uma opção (1-6): ").strip()
        
        # OPÇÃO 1
        if opcao == "1":
            exibir_lista(cardapio, "Cardápio Completo")
            
        # OPÇÃO 2
        elif opcao == "2":
            termo = input("\nDigite o nome ou ingrediente para buscar: ")
            buscar_drink(termo, cardapio)
             
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
            print("\nSaindo da Conta")
            break
            
        # OPÇÃO INVÁLIDA
        else:
            print("\n⚠️ Opção inválida! Digite um número de 1 a 6.")



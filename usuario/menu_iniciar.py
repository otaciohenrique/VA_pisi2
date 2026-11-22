from usuario.login import login_usuario
from usuario.cadastro import cadastrar_usuario
from sistema.menu_usuario import menu_usuario
from rich.console import Console
from rich.table import Table
from rich import box
from rich.panel import Panel

console = Console()

def menu_iniciar():
    while True:
            console.clear ()
            painel = Panel("[bold blue] CATÁLOGO DE COQUETÉIS [/]", border_style="blue", expand=False)
            console.print(painel)
            
            tabela = Table(
            show_header=False, 
            box=box.ROUNDED
            )

            tabela.add_column("Opção", justify="center", style="bold white", no_wrap=True)
            tabela.add_column("Ação", style="white")


            tabela.add_row("1.", "Login")
            tabela.add_row("2.", "Novo Usuário")
            tabela.add_row("3.", "Sair")

            print()
            console.print(tabela)
    
            
            opcao = input("\nEscolha uma opção (1-3): ").strip()
            
            # OPÇÃO 1
            if opcao == "1":
                login_usuario()
                menu_usuario()
                
                
            # OPÇÃO 2
            elif opcao == "2":
                cadastrar_usuario()

            # OPÇÃO 3
            elif opcao == "3":
                print("\nSaindo do sistema.")
                break
                             
            # OPÇÃO INVÁLIDA
            else:
                print("\n⚠️ Opção inválida! Digite um número de 1 a 3.")


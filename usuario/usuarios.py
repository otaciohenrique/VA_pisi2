from rich.console import Console
from rich.table import Table
from rich import box
from rich.panel import Panel

console = Console()

class Usuario:
    def __init__(self, nome, senha, data_nasc):
        self.__nome = nome
        self.__senha = senha
        self.__data_nasc = data_nasc

    def get_nome(self):
        return self.__nome

    def verificar_senha(self, senha_digitada):
        return self.__senha == senha_digitada

    def atualizar_nome(self, novo_nome):
        if novo_nome != "":
            self.__nome = novo_nome
            return True
        return False

    def atualizar_senha(self, nova_senha):
        if nova_senha != "":
            self.__senha = nova_senha
            return True
        return False


usuarios = [
    Usuario("otacio", "123", "19/05/2000"),
]


usuarios = [
    Usuario("otacio", "123", "19/05/2000"),
]


def configuracao(usuario_logado):
    while True:
        console.clear()
        painel = Panel("[bold blue] CONFIGURAÇÕES DE USUÁRIO [/]", border_style="blue", expand=False)
        console.print(painel)
                
        tabela = Table(show_header=False, box=box.ROUNDED)
        tabela.add_column("Opção", justify="center", style="bold white", no_wrap=True)
        tabela.add_column("Ação", style="white")
    
        tabela.add_row("1.", "Editar Nome de Usuário")
        tabela.add_row("2.", "Editar Senha")
        tabela.add_row("3.", "Excluir Conta")
        tabela.add_row("4.", "Sair")
    
        print()
        console.print(tabela)
                
        opcao = input("\nEscolha uma opção (1-4): ").strip()

        if opcao == "1":
            console.print("\n[bold yellow]--- Editar Nome de Usuário ---[/bold yellow]")
            # Acessamos o atributo com ponto (.) em vez de colchetes ["nome"]
            console.print(f"Nome atual: [bold]{usuario_logado.nome}[/bold]")
            
            novo_nome = console.input("Digite o novo nome de usuário: ").strip()
            
            # Usamos o método da classe para atualizar
            if usuario_logado.atualizar_nome(novo_nome):
                console.print(f"\n[bold green]✅ Nome atualizado para '{novo_nome}' com sucesso![/bold green]")
            else:
                console.print("\n[bold red]⚠️ O nome não pode ficar vazio![/bold red]")
                
            console.input("\n[gray]Pressione ENTER para continuar...[/gray]")

        elif opcao == "2":
            console.print("\n[bold yellow]--- Editar Senha ---[/bold yellow]")
            senha_atual = console.input("Digite sua senha atual para confirmar: ").strip()
            
            # Usamos o método da classe para validar a segurança
            if usuario_logado.verificar_senha(senha_atual):
                nova_senha = console.input("Digite a nova senha: ").strip()
                
                if usuario_logado.atualizar_senha(nova_senha):
                    console.print("\n[bold green]✅ Senha atualizada com sucesso![/bold green]")
                else:
                    console.print("\n[bold red]⚠️ A senha não pode ficar vazia![/bold red]")
            else:
                console.print("\n[bold red]⚠️ Senha incorreta![/bold red]")
                
            console.input("\n[gray]Pressione ENTER para continuar...[/gray]")

        elif opcao == "3":
            console.print("\n[bold red]--- Excluir Conta ---[/bold red]")
            
            senha_atual = console.input("Digite sua senha para confirmar a exclusão: ").strip()
            
            if usuario_logado.verificar_senha(senha_atual):
                confirmacao = console.input(f"[bold red]Tem certeza que deseja excluir sua conta de forma permanente, {usuario_logado.nome}? (S/N): [/bold red]").strip().upper()
                
                if confirmacao == "S":
                    usuarios.remove(usuario_logado)
                    console.print("\n[bold green]🗑️ Conta excluída com sucesso![/bold green]")
                    console.input("\n[gray]Pressione ENTER para sair...[/gray]")
                    break
                else:
                    console.print("\n[bold yellow]Exclusão cancelada.[/bold yellow]")
                    console.input("\n[gray]Pressione ENTER para continuar...[/gray]")
            else:
                console.print("\n[bold red]⚠️ Senha incorreta! Exclusão cancelada.[/bold red]")
                console.input("\n[gray]Pressione ENTER para continuar...[/gray]")

        elif opcao == "4":
            break

        else:
            console.print("\n⚠️ Opção inválida! Digite um número de 1 a 4.")
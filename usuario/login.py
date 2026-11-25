from usuario.usuarios import usuarios 
from rich.console import Console
from rich.panel import Panel

console = Console()

def login_usuario():
    console.clear ()

    painel = Panel("[bold blue] LOGIN [/]", border_style="blue", expand=False)
    console.print(painel)

    print()

    usuario = nome_usuario()
    senha_salva = usuario["senha"]
    senha_usuario(senha_salva)

    return usuario

def nome_usuario():
    while True:
        nome_digitado = console.input("[bold blue] Usuário: ").strip()
        if nome_digitado == "":
            console.print ("⚠️ Erro: O Nome de Usuário não pode ficar em branco. ⚠️")
            continue

        usuario_encontrado = False
        for usuario_salvo in usuarios:
            if usuario_salvo["nome"] == nome_digitado:
                usuario_encontrado = True
                break
        if not usuario_encontrado:
            console.print("Nome de Usuário não encontrado")
        else:
            return usuario_salvo

def senha_usuario(senha_correta):
     while True:
        senha_digitada = console.input("[bold blue] Senha: ").strip()
        if senha_digitada == "":
            console.print ("⚠️ Erro: A Senha não pode ficar em branco. ⚠️")
            continue

        elif senha_digitada == senha_correta:
            return senha_correta
        else:
            console.print ("⚠️  Senha Incorreta ⚠️") 
            


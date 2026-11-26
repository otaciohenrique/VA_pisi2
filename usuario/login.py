from usuario.usuarios import usuarios 
from rich.console import Console
from rich.panel import Panel
import os

console = Console()

def login_usuario():
    os.system('cls')

    painel = Panel("[bold blue] LOGIN [/]", border_style="blue", expand=False)
    console.print(painel)

    console.print()

    usuario = nome_usuario()
    
    # MUDANÇA: Passamos o objeto 'usuario' inteiro para verificação, sem expor a senha
    senha_usuario(usuario)

    return usuario

def nome_usuario():
    while True:
                
        nome_digitado = console.input("[bold blue] Usuário: ").strip()
        if nome_digitado == "":
            console.print ("⚠️ Erro: O Nome de Usuário não pode ficar em branco. ⚠️")
            continue

        usuario_encontrado = None
        for usuario_salvo in usuarios:            
            if usuario_salvo.get_nome() == nome_digitado:
                usuario_encontrado = usuario_salvo
                break
                
        if not usuario_encontrado:
            console.print("Nome de Usuário não encontrado")
        else:
            return usuario_encontrado

def senha_usuario(usuario_encontrado):
    while True:
        senha_digitada = console.input("[bold blue] Senha: ").strip()
        if senha_digitada == "":
            console.print ("⚠️ Erro: A Senha não pode ficar em branco. ⚠️")
            continue

        # MUDANÇA: Utilizamos o método nativo do objeto para validar a segurança
        elif usuario_encontrado.verificar_senha(senha_digitada):
            return True
        else:
            console.print ("⚠️  Senha Incorreta ⚠️")
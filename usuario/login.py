from usuarios import usuarios 

def login():
    print("\n--- LOGIN ---")
    usuario = nome_usuario()
    senha_salva = usuario["senha"]
    senha_usuario(senha_salva)

def nome_usuario():
    while True:
        nome_digitado = input("Nome de Usuário: ").strip()
        if nome_digitado == "":
            print ("⚠️ Erro: O Nome de Usuário não pode ficar em branco. ⚠️")
            continue

        usuario_encontrado = False
        for usuario_salvo in usuarios:
            if usuario_salvo["nome"] == nome_digitado:
                usuario_encontrado = True
                break
        if not usuario_encontrado:
            print("Nome de Usuário não encontrado")
        else:
            return usuario_salvo

def senha_usuario(senha_correta):
     while True:
        senha_digitada = input("Senha: ").strip()
        if senha_digitada == "":
            print ("⚠️ Erro: A Senha não pode ficar em branco. ⚠️")
            continue

        elif senha_digitada == senha_correta:
            return senha_correta
        else:
            print ("⚠️  Senha Incorreta ⚠️") 
            


from datetime import datetime
from usuario.usuarios import usuarios 

def cadastrar_usuario():
    while True:
        print("\n--- CADASTRO DE USUÁRIO ---")
        data_nasc = cadastro_data_nasc()

        if data_nasc is not None:
            nome_u = cadastro_nome()
            senha = cadastro_senha()

            novo_usuario = {
                "nome": nome_u,
                "senha": senha,
                "data_nasc": data_nasc
  
            }
            usuarios.append(novo_usuario)
            print("\n✅ Cadastro realizado com sucesso!")
            return

def cadastro_data_nasc():
    while True:
        print ("Digite no formato (DD/MM/AAAA):")
        data_str = input("Data de nascimento ").strip()
        try:
            data_nasc = datetime.strptime(data_str, "%d/%m/%Y")
            hoje = datetime.now()
            idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
            
            if idade >= 18:
                return data_str 
            else:
                print("❌ Cadastro bloqueado: Proibido para menores de 18 anos")
                return None 
                
        except ValueError:
            print("⚠️ Inválido! Digite no formato DD/MM/AAAA. ⚠️")

def cadastro_nome():
    while True:
        nome = input("Escolha o nome de usuário: ").strip()
        if nome == "":
            print ("⚠️ Erro: O nome não pode ficar em branco. ⚠️")
            continue

        nome_existente = False
        for usuario_salvo in usuarios:
            if usuario_salvo["nome"] == nome:
                nome_existente = True
                break
        if nome_existente:
            print("⚠️ Erro: Este nome de usuário já está em uso. Escolha outro. ⚠️")
        else:
            return nome
        
def cadastro_senha():
    while True:
        print("\nA senha deve ter pelo menos 8 caracteres e incluir letras maiúsculas, minúsculas e números.")
        senha = input("Escolha uma senha: ").strip()

        if len(senha) < 8:
            print("⚠️ Erro: A senha precisa ter 8 ou mais caracteres.")
            continue

        tem_maiuscula = False
        tem_minuscula = False
        tem_numero = False

        for caractere in senha:
            if caractere.isupper():
                tem_maiuscula = True
            elif caractere.islower():
                tem_minuscula = True
            elif caractere.isdigit():
                tem_numero = True

        if tem_maiuscula and tem_minuscula and tem_numero:
            return senha
        else:
            print("⚠️ Erro: Tente a senha novamente ⚠️")


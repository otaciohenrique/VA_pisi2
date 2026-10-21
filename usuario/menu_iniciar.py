from usuario.login import login_usuario
from usuario.cadastro import cadastrar_usuario
from sistema.menu_usuario import menu_usuario

def menu_iniciar():
    while True:
            print("\n" + "="*30)
            print(" LOGIN")
            print("="*30)
            print("1. Login")
            print("2. Novo Usuário")
            print("3. Sair")
            
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


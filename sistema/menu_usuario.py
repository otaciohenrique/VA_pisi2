from sistema.cardapio import cardapio 
from sistema.utils import exibir_lista
from sistema.buscar import buscar_drink
from sistema.adicionar import adicionar_drink
from sistema.editar import editar_drink
from sistema.deletar import deletar_drink


# MENU 
def menu_usuario():
    while True:
        print("\n" + "="*30)
        print(" CATÁLOGO DE COQUETÉIS")
        print("="*30)
        print("1. Mostrar Todos os Drinks")
        print("2. Buscar Drink ou Ingrediente")
        print("3. Adicionar Novo Drink")
        print("4. Editar um Drink")
        print("5. Deletar um Drink")
        print("6. Sair")
        
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
            print("\nSaindo do sistema...")
            break
            
        # OPÇÃO INVÁLIDA
        else:
            print("\n⚠️ Opção inválida! Digite um número de 1 a 6.")



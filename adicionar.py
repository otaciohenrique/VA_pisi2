# ADICIONAR
def adicionar_drink(lista_cardapio):
    print("\n--- Adicionar Novo Drink ---")
    nome = input("Nome do drink: ").strip()
    ingredientes_texto = input("Ingredientes: ").strip()
            
    if nome == "" or ingredientes_texto == "":
        print("⚠️ Erro: Nome e ingredientes não podem ficar em branco.")
    else:
        lista_ingredientes = [ingrediente.strip() for ingrediente in ingredientes_texto.split(",")]
        novo_drink = {"nome": nome, "ingredientes": lista_ingredientes}
        lista_cardapio.append(novo_drink)
        print(f"✅ Drink '{nome}' adicionado com sucesso!")


def limpar_texto(texto):
    texto = texto.lower().strip()
    
    acentos = "áàãâéêíóõôúç"
    sem_acentos = "aaaaeeiooouc"
    
    for i in range(len(acentos)):
        texto = texto.replace(acentos[i], sem_acentos[i])
        
    return texto

 
def exibir_lista(lista_drinks, titulo="Cardápio"):
    print(f"\n--- {titulo.upper()} ---")
    if len(lista_drinks) == 0:
        print("Nenhum drink encontrado.")
    else:
        lista_ordenada = sorted(lista_drinks, key=lambda d: d["nome"])

        for i, drink in enumerate(lista_ordenada, 1):
            ingredientes_texto = ", ".join(drink["ingredientes"])
            print(f"{i}. {drink['nome']}")
            print(f"   Ingredientes: {ingredientes_texto}")
    print("-" * 30)
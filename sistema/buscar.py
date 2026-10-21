from sistema.utils import limpar_texto, exibir_lista

def buscar_drink(termo, lista_cardapio):
    resultados = []
    termo_limpo = limpar_texto(termo)
    
    for drink in lista_cardapio:
        nome_limpo = limpar_texto(drink["nome"])
        
        if termo_limpo in nome_limpo:
            resultados.append(drink)
            continue 
        
        for ingrediente in drink["ingredientes"]:
            ingrediente_limpo = limpar_texto(ingrediente)
            if termo_limpo in ingrediente_limpo:
                resultados.append(drink)
                break 
                
    exibir_lista(resultados, f"Resultados para '{termo}'")


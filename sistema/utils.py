from rich.console import Console

console = Console()

def limpar_texto(texto):
    texto = texto.lower().strip()
    
    acentos = "áàãâéêíóõôúç"
    sem_acentos = "aaaaeeiooouc"
    
    for i in range(len(acentos)):
        texto = texto.replace(acentos[i], sem_acentos[i])
        
    return texto

 

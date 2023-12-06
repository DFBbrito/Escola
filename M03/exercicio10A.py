"""
cesar
"""
alfabeto="abcdefghijklmnopqrstuvwxyz"
codigo="bcdefghijklmnopqrstuvwxyza"

def Codifica(texto):
    """Recebe um texto e devolver o texto codificado"""
    global alfabeto, codigo
    codificado=""
    texto=texto.lower()
    for letra in texto:
        if letra in alfabeto:
            posicao = alfabeto.index(letra)
            codificado += codigo[posicao]
        else:
            codificado+=letra

def Descodifica(texto):
    """Recebe um texto codificado e descodifica"""
    pass## mesmo codigo alfabeto muda


print(Codifica("Bebe"))
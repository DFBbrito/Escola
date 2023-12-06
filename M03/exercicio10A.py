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
    print(codificado)

def Descodifica(texto):
    """Recebe um texto codificado e descodifica"""
    global alfabeto, codigo
    descodificado=""
    texto=texto.lower()
    for letra in texto:
        if letra in codigo:
            posicao = codigo.index(letra)
            descodificado += alfabeto[posicao]
        else:
            descodificado+=letra
    print(descodificado)

print(Codifica("Bebe"))
print(Descodifica("Bebe"))
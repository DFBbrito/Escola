"""
2-Escreve uma funçao que receba um dicionario como entrada e retorne a soma de todos os valores numericos
"""
def soma_valores_numericos(dicionario):
    soma=0
    for valor in dicionario.values():
        if type(valor) in (int, float):
            soma+=valor
    return soma

dicionario={'a':1,'b':2,'c':'texto','d':4.5,'e':True}
resultado=soma_valores_numericos(dicionario)
print("A soma dos valores numéricos é:",resultado)

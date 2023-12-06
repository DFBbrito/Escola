"""
Correçao
1. Crie uma funçao que recebe dois paramentros. a funçao deve calcular e mostrar a soma de todos os numeros
entre os dois parametros.
"""
def Somatorio(x1,x2):
    soma=0
    for x in range(x1,x2+1):
        soma=soma+x
    print(soma)


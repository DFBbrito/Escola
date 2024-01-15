#Daniel Brito
"""
Utilizando funçoes crie um programa que lê 5 valores para um array e mais 5 para outro.
O programa deve mostrar a soma total de todos os valores dos dois arrays.
"""
import numpy as np

#definir o max dos elementos
MAX_ITEMS=5

#definir os arrays
numeros1=np.empty(MAX_ITEMS,dtype='i')
numeros2=np.empty(MAX_ITEMS,dtype='i')

#funçao para ler os dados para os vetores
def ler_dados(numeros):
    """Funçao que recebe um array e preenche com dados do utilizador"""
    for pos in range(MAX_ITEMS):
        numeros[pos]=int(input('Insrira um nº:'))

#somar e mostrar o total 
def somar_dados(numeros):
    """Funçao que recebe um array e devolve a soma total dos valores"""
    soma=0
    for x in numeros:
        soma+=x
    return soma

ler_dados(numeros1)
ler_dados(numeros2)
soma=somar_dados(numeros1)+somar_dados(numeros2)

print(soma)

#Daniel Brito
"""
Crie um programa que lê 5 valores para um array e mais 5 para outro.
O programa deve mostrar a soma total de todos os valores dos dois arrays.
"""
import numpy as np

#definir o max dos elementos
MAX_ITEMS=5

#definir os arrays
numeros1=np.empty(MAX_ITEMS,dtype='i')
numeros2=np.empty(MAX_ITEMS,dtype='i')

#ler os dados para os vetores
for pos in range(MAX_ITEMS):
    numeros1[pos]=int(input('Insrira um nº:'))

for pos in range(MAX_ITEMS):
    numeros2[pos]=int(input('Insrira um nº:'))

#somar e mostrar o total 
soma=0
for pos in range(MAX_ITEMS):
    soma+=numeros1[pos]

for pos in range(MAX_ITEMS):
    soma+=numeros2[pos]

print(soma)

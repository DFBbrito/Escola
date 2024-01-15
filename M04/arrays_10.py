#Daniel Brito
"""
Programa que cria um array de 1000 posiçoes e preenche cada posiçao 
com um nº de 1 a 1000
"""
import numpy as np

#DEFINIR o numero maximo de elementos 
MAX_ITEMS=1000

#definir o array
numeros=np.zeros(MAX_ITEMS,dtype='i')

#preencher o array
for pos in range(MAX_ITEMS):
    numeros[pos]=pos+1

#mostrar os valores do array
print(numeros)

#mostrar por ordem inversa
for pos in range(MAX_ITEMS-1,-1,-1):
    print(numeros[pos])

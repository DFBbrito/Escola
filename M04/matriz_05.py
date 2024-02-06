"""
um programa para criar uma matriz com os valores
a 0 com exceção da diagonal principal deve ficar a 1
"""
import numpy as np 

FORMA=(10,10)

matriz=np.zeros(FORMA,'i')

for d in range(matriz.shape[0]):
    matriz[d,d]=1

print(matriz)
"""
Substituição de Elementos: Dada uma matriz,
substitua todos os elementos negativos por zero.
"""
import numpy as np 

FORMA=(10,10)

matriz=np.array([[1,2,3,-7],[1,-2,33,0],[1,4,-3,0]])

for l in range(matriz.shape[0]):
    for c in range(matriz.shape[1]):
        if matriz[l,c]<0:
            matriz[l,c]=0

print(matriz)
"""
Soma de Matrizes: 
Dadas duas matrizes 2D, escreva um programa para 
calcular a soma delas.
"""
import numpy as np
import random

FORMA=(2,2)

m1=np.array([[1,2],[3,4]])
m2=np.array([[5,6],[7,8]])
m3=np.empty(FORMA,'i')

for l in range(m1.shape[0]):
    for c in range(m1.shape[1]):
        m3[l,c]=m1[l,c]+m2[l,c]

print(m1)
print("+")
print(m2)
print("=")
print(m3)


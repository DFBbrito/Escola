"""
Soma de Matrizes: 
Dadas duas matrizes 2D, escreva um programa para 
calcular a soma delas.
"""
import numpy as np
import matriz_01_v2

FORMA=(2,2)

m1=np.array([[1,2],[3,4]])
m2=np.array([[5,6],[7,8]])

m1=matriz_01_v2.preenche(m1)
m2=matriz_01_v2.preenche(m2)

#soma duas matrizes e devolve a soma numa terceira matriz
def soma_matrizes(m1,m2):
    m3=np.empty((m1.shape[0],m1.shape[1]))    
    for l in range(m1.shape[0]):
        for c in range(m1.shape[1]):
            m3[l,c]=m1[l,c]+m2[l,c]
    return m3

m3=soma_matrizes(m1,m2)
print(m3)

#soma duas matrizes e guarda no terceiro parametro
def soma_matrizes_v2(m1,m2,m3):
    for l in range(m1.shape[0]):
        for c in range(m1.shape[1]):
            m3[l,c]=m1[l,c]+m2[l,c]
    
m4=np.zeros(FORMA)
soma_matrizes_v2(m1,m2,m4)
print(m4)
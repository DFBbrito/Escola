"""
Inicialização de Matriz: Crie uma matriz 2D de tamanho 3x3 e preencha-a com valores inteiros aleatórios.
"""
import numpy as np 
import random

FORMA=(3,3)

matriz=np.zeros(FORMA,'i')
#empty esta vazio mas com lixo
#zeros esta com zeros
#array meter sempre valores
for l in range(3):
    for c in range(3):
        matriz[l,c]=random.randint(1,100)
print(matriz)

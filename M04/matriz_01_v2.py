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

def preenche(matriz):        
    for l in range(matriz.shape[0]):
        for c in range(matriz.shape[1]):
            matriz[l,c]=random.randint(1,100)
    return matriz

def main():
    FORMA=(3,3)
    matriz=np.zeros(FORMA,'i')
    print(preenche(matriz))
    
if __name__=="__main__":
    main()



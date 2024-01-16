#Daniel Brito
"""Programa para ler 10 numeros e guardar um array"""
import numpy as np

MAX_VETOR=10

#criar array
vetor=np.empty(MAX_VETOR)

#ler os valores
for i in range(len(vetor)):
    vetor[i]=int(input("Insira um nº:"))

#erro pq não exite a posição 10
#print(vetor[10])
    
#mostrar os valores por ordem inversa
for i in range(MAX_VETOR-1,-1,-1):
    print(vetor[i])
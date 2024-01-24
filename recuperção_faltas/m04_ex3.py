"""
Crie um programa que lê 10 valores do utilizador e calcula a média. 
"""
import numpy as np
 
MAX_ITEMS = 10
numeros = np.empty(MAX_ITEMS)
soma = 0
 
for i in range(MAX_ITEMS):
    numeros[i] = int(input("Nº:"))
    soma = soma + numeros[i]
 
media = soma / MAX_ITEMS
print(f"A média dos valores introduzidos é {media}")
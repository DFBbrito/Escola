"""
Altere o programa anterior de forma que mostre quantos valores são superiores à média. 
"""
import numpy as np

MAX_ITEMS=10
numeros=np.empty(MAX_ITEMS)
soma=0

for i in range(MAX_ITEMS):
    numeros[i]=int(input("Nº:"))
    soma=soma+numeros[i]

media=soma/MAX_ITEMS
print(f"A média é {media}")

superiores_media = 0

for valor in numeros:
    if valor > media:
        superiores_media += 1

print(f"{superiores_media} valores são superiores à média.")

#ja esta

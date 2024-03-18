"""
Crie um programa que mostra o maior e o menor valores de um array.
"""
import numpy as np

values=np.zeros(10,int)

for i in range(10):
    value=int(input("valor:"))
    values[i]=value

max_value=np.max(values)
min_value=np.min(values)

print(f"maior{max_value}- minimo{min_value}")
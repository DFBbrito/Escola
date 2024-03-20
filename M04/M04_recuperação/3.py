"""
Crie um programa que lê 10 valores do utilizador e calcula a média.
"""
import numpy as np

values=np.zeros(10,int)

for i in range(10):
    value=int(input("Introduza um valor: "))
    values[i]=value

mean=np.mean(values)
print(f"media {mean}")

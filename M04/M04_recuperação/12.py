"""
Crie um programa que ordena os valores de um array por ordem crescente.
"""
import numpy as np

values = np.zeros(10, dtype=int)

for i in range(10):
    value = int(input("Introduza um valor: "))
    values[i] = value

values = np.sort(values)
print("Valores ordenados por ordem crescente: ", values)
"""
Altere o programa anterior para ordenar por ordem decrescente.
"""
import numpy as np

values = np.zeros(10, dtype=int)

for i in range(10):
    value = int(input("Introduza um valor: "))
    values[i] = value

values = np.sort(values)[::-1]
print("Valores ordenados por ordem decrescente: ", values)

"""
Crie um programa que lê 10 valores e mostre quais desses valores são repetidos e quantas vezes se repetem
"""
import numpy as np

values=np.zeros(10,int)

for i in range(10):
    value=int(input("valor:"))
    values[i]=value

unique_values, counts = np.unique(values, return_counts=True)

for i in range(len(unique_values)):
    print("Valor: ", unique_values[i], " - Repetições: ", counts[i])
    
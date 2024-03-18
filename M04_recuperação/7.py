"""
Crie um programa que lê 5 valores para um array e mais 5 para outro. O programa deve mostrar a soma total de todos os valores dos dois arrays.
"""
import numpy as np

values1=np.zeros(5,int)
values2=np.zeros(5,int)

for i in range(5):
    value=int(input("valor:"))
    values1[i]=value

for i in range(5):
    value=int(input("valor:"))
    values2[i]=value

sumvalues=np.sum(values1)+np.sum(values2)
print(f"soma total {sumvalues}")
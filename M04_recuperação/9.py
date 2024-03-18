"""
Crie um programa que lê 5 valores para um array inserindo os dados por ordem crescente.
"""
import numpy as np

values =np.zeros(5,int)

for i in range(5):
    value=int(input("Valor:"))
    if i == 0:
        values[i]=value
    else:
        for j in range(i):
            if value<values[j]:
                values[j:i]=values[j+1:i+1]
                values[j]=value
                break
            elif j ==i-1:
                values[j+1]=value

print("valores inversos",values)

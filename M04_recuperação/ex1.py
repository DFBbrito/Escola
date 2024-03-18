"""
a)	Faça um programa que leia um array de 5 números inteiros e os exiba.
 1.	Mostre a média dos números inseridos com até 2 casas decimais.
"""
import numpy as np

arr=np.zeros(5)

for i in range(5):
    numeros=float(input("nº:"))
    arr[i]=numeros

soma=0
for i in range(5):
    soma+=arr[i]
    print(arr[i])

media=soma/5
print(f"A media é {media:.2f}")

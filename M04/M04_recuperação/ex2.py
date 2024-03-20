"""
b)	Crie um programa que leia um array de 10 números reais e os mostre na ordem inversa.
 1.	Mostre qual a percentagem de números positivos e negativos.
"""
import numpy as np

arr=np.empty(10)

for i in range(10):
    arr[i]=float(input("nº:"))

for i in range(9,-1,-1):
    print(arr[i])

contar=0
for x in arr:
    if x<0:
        contar+=1

contar_positivos=10-contar
p_p=contar_positivos/10*100
p_n=contar/10*100
print(f"{p_p} \n {p_n}")

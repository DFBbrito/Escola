#Daniel Brito
"""
um programa que vai inverter as posiçoes dos dados de um array
p.ex: 1 2 3 4 => 4 3 2 1  
"""
import numpy as np

numeros=np.array([1,2,3,4,5])
temp=np.empty(5,dtype='i')

#inverter as posiçoes dos valores
for i in range(len(numeros)):
    temp[i]=numeros[len(numeros)-1-i]

#print(temp)
numeros=temp
print(numeros)
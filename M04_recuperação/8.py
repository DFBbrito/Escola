"""
Altere o programa anterior para mostrar a soma dos valores de cada posição dos dois arrays, ou seja, soma o valor daprimeira posição de um array com o valor na mesma posição do outro e assim sucessivamente.
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

sumvalues=values1 + values2
print(sumvalues)
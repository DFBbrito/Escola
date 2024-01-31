"""
Altere o programa anterior para listar os valores por ordem inversa. 
"""
import numpy as np

valores=np.zeros(10)

for i in range(10):
    valor=float(input(f"Digite o {i + 1} valor: "))
    valores[i]=valor

inver=np.empty(10, dtype='float')
indice2=len(valores) - 1

for i in range(len(valores)):
    inver[i]=valores[indice2]
    indice2-=1

for valor in inver:
    print(valor)



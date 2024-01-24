"""
Crie um programa que utiliza um array de 1 dimensão para guardar 10 valores. 
Os valores devem ser introduzidos pelo utilizador e, antes de terminar, o programa deve 
listar todos os valores do array. 
"""
import numpy as np

valores=np.zeros(10)

for i in range(10):
    valor=float(input(f"Digite o {i + 1} valor: "))
    valores[i]=valor


for valor in valores:
    print(valor)

   
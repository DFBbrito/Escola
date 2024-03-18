"""
Crie um programa que utiliza um array de 1 dimensão para guardar 10 valores. Os valores devem ser introduzidos pelo utilizador e, antes de terminar, o programa deve listar todos os valores do array.
"""
import numpy as np

values=np.zeros(10, dtpye=int)

for i in range(10):
    value=int(input("Introduza um valor: "))
    values[i]=value

print(f"Valores:{values}")

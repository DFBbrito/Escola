"""
Altere o programa anterior para listar os valores por ordem inversa
"""
import numpy as np

values=np.zeros(10,int)

for i in range(10):
    value=int(input("Introduza um valor:"))
    values[i]=value

print(f"valores:{values} Inversa {values[::-1]}")
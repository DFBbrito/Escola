import numpy as np 

def FunçaoContem(nomes,nome_a_contar):
    contar=0
    for n in nomes:
        if n==nome_a_contar:
            contar+=1
    return contar

n=np.array(["Maria","Maria","Joaquim","António"])
print(FunçaoContem(n,"Maria"))
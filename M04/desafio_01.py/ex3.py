import numpy as np 

def FunçaoContem(nomes):
    if "Joaquim" in nomes:
        return True
    return False

def FunçaoContemV2(nomes):
    for n in nomes:
        if n=="Joaquim":
            return True
        return False

n=np.array(["Maria","Joaquim","António"])
print(FunçaoContem(n))
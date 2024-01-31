#daniel brito
"""
Implemente uma funçao que remove todos os numeros duplicados de uma array.
Por exemplo, transformar [1,2,2,3,3,3,4] em [1,2,3,4,0,0,0].
"""
import numpy as np 

def RemoveDuplicados(arr):
    temp=np.zeros(len(arr))
    pos=0
    for i in range(len(arr)):
        #se o nº ñ existir em temp
        if arr[i] in temp:
            continue
        else:
            temp[pos]=arr[i]
            pos+=1
    arr[:]=temp
    return arr

print(RemoveDuplicados([1,2,2,3,3,3,4]))
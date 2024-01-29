"""
Crie um programa para sortear os números do euro milhões. 
Devemos sortear 5 números entre 1 e 50 e mais 2 números entre 1 e 12. 
Os números sorteados não se podem repetir. 
Devemos mostrar os números por ordem crescente.
"""
import random 
import numpy as np

def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                t=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=t
    return arr

#arrays para guardar nº
numeros=np.zeros(5,'i')
estrelas=np.zeros(2,'i')

i=0
while i<5:
    #sortear um nº de 1 a 50 inclusive
    x=random.randint(1,50)
    #verificar repetido
    if x in numeros:
        continue
    numeros[i]=x
    i+=1
#print(bubble_sort(numeros))
#print(np.sort(numeros))

n=0
while n<2:
    #sortear um nº de 1 a 12 inclusive
    y=random.randint(1,12)
    #verificar repetido
    if x in estrelas:
        continue
    estrelas[n]=y
    n+=1
#print(bubble_sort(estrelas))
#print(np.sort(estrelas))   

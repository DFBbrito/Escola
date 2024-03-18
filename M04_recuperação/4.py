"""
Altere o programa anterior de forma que mostre quantos valores são superiores à média.
"""
import numpy as np

values=np.zeros(10,int)

for i in range(10):
    value=int(input("Introduza:"))
    values[i]=value

mean=np.mean(values)
print("Media",mean)

count=np.sum(values>mean)
print("superior a media",count)

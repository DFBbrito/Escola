import numpy as np

MAX_ITEMS=5

nomes=np.empty(MAX_ITEMS,"u20")
tempos=np.empty("Nome:")

#ler os dados
for i in range(MAX_ITEMS):
    nomes[i]=input("Nome:")
    tempos[i]=int(input("Tempo:"))

#melhor e pior tempos
melhor=tempos[0]
pos_melhor=0
pior=tempos[0]
pos_pior=0
for i in range(MAX_ITEMS):
    if pior<tempos[i]:
        pior=tempos[i]
        pos_pior=i
    if melhor>tempos[i]:
        melhor=tempos[i]
        pos_melhor=i

#primeiro
print(nomes[pos_melhor])
#ultimo
print(nomes[pos_pior])
#diferença 
diferenca=pior-melhor
print(diferenca)

#mostrar os nomes e os tempos
for i in range(MAX_ITEMS):
    print(f"Nome: {nomes[i]} - Tempo: {tempos[i]}")
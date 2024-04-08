import numpy as np

nomes=np.zeros(5,object)
tempo=np.zeros(5,int)

#nome do piloto
for i in range(5):
    nome=input("Diga o nome:")
    nomes[i]=nome
#tempo gasto na corrida
    temp=int(input("Diga o tempo:"))
    tempo[i]=temp

#imprimir o primeiro e ultimo e respetivos tempos


#listar todos os participantes e o seu tempo
print(f"Pilotos: {nomes}, \nTempo: {tempo}")
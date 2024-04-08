#Daniel Brito
import numpy as np 

local=np.array([])
golos=np.array([])
jogos_casa=np.array([])
jogos_fora=np.array([])

while True:
    local=str(input("Em que cidade foi o jogo? "))
    golos=int(input("Quantos golos marcaram?"))
    if local == "Viseu":
        jogos_casa+=1
    elif local != "Viseu":
        jogos_casa+=1
    if golos<=0:
        print("valor de golos incorreto")
    
    


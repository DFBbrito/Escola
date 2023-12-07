#Daniel Brito
"""
Jogo(pedra, papel ou tesoura)

"""
"""Implemntar o jogo pedra papel ou tesoura"""

import random
def CPU_Joga():
    """Devolve a jogada do cpu"""
    opçao=random.randint(1,3)
    if opçao==1:
        return "pedra"
    elif opçao==2:
        return "papel"
    else:
        return "tesoura"

def Player_Joga():
    """Lê a jogada do utilizador"""
    #fazer validaçao
    while True:
        escolha=input("Escolha pedra,papel ou tesoura: ")
        if escolha in ("tesoura","papel","pedra"):
            break
    return escolha

def Vitoria(p1,p2):
    if p1=="pedra" and p2=="tesoura":
        return True
    if p1=="tesoura" and p2=='papel':
        return True
    if p1=="papel" and p2=="pedra":
        return True
    return False

def Testar_Vitoria(Jogada_pc,jogada_player):
    """Indica se alguém ganhou"""
    print(f'Computador: {Jogada_pc}')
    print(f'Player: {jogada_player}')
    Vitoria(Jogada_pc,jogada_player)
    Vitoria(jogada_player,Jogada_pc)
    if Vitoria(Jogada_pc,jogada_player)==True:
        print('Computador ganha!')
        return True
    if Vitoria(jogada_player,Jogada_pc)==True:
        print('player ganha')
        return True
    return False 

def main():
    while True:
        jogada_cpu=CPU_Joga()
        jogada_player=Player_Joga()
        alguem_ganhou=Testar_Vitoria(jogada_cpu,jogada_player)
        if alguem_ganhou==True:
            break
        else:
            print("empate!")

if __name__=="__main__":
    main()


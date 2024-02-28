"""
-> lista sócios do sporting (nomes)
-> lista sócios do benfica (nomes)
-> remover das duas listas sócios que existem nas duas listas
"""
import numpy as np 

#Ler os sócios
#perguntar o nº de socios ou terminar qaundo inserir um nome em branco
def LerNomes(lista):
    n=int(input("Indique o nºr de sócios:"))
    for _ in range(n):
        nome=input("Indique um nome:")
        lista.append(nome)

#comparar as duas listas
#percorrer uma lista e verificar se o nome exite na outra
#se existir remover
def RemoveRepetidos(lista1,lista2):
    #remove os elmentos que existem nas duas listas
    #for nomes in lista1[:]:
    for posiçao in range(len(lista1)-1,-1,-1):
        if lista1[posiçao] in lista2:
            lista2.remove(lista1[posiçao])
            nome=lista1.pop(posiçao)
            print(f"O nome {nome} foi removido das duas listas")


def main():
    #criar duas listas vazias
    clube1=[]
    clube2=[]
    #ler os dados para uma lista
    LerNomes(clube1)
    #ler os dados para outra lista
    LerNomes(clube2)
    print(clube1)
    print(clube2)
    RemoveRepetidos(clube1,clube2)
    print(clube1)
    print(clube2)
    
if __name__ == "__main__":
    main()
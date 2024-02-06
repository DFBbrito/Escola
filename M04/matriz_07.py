"""
Fazer um programa para gerir os contactos de uma agenda. 
Deve permitir adicionar nome e telefone de cada contacto. 
Deve permitir listar todos e pesquisar por um nome.
Deve permitir Alterar o telefone de um nome.
"""
import numpy as np

#menu
#1. Adicionar novo
#2. Listar Todos
#3. Pesquisar por nome
#4. Alterar telefone com base no nome
#5. Terminar

def menu():
    print('1.Adicionar\n2.listar\n3.Pesquisar\n4.Editar\n5.Terminar')
    op=input(":")
    return op

#funçao para adicionar novo contacto e devolve o nr de contactos
def Add(contactos,nr_contactos):
    nome=input('Digite o nome:')
    numero=input("numero:")
    #guardar na matriz
    contactos[nr_contactos,0]=nome
    contactos[nr_contactos,1]=numero
    nr_contactos+=1
    #devolve o nr de contactos
    return nr_contactos


def Listar(contactos,nr_contactos):
    for l in range(nr_contactos)
        print(f"Nome:{contactos[l,0]} - Telefone: {contactos[l,1]}")

def Pesquisa():
    pass

def Alterar():
    pass

def Terminar():
    pass

def main():
    #matriz vai ter 100 linhas e 2 colunas
    FORMA=(100,2)
    contactos=np.empty(FORMA,'uso') #strings com 50 letras cada no máximo
    nr_contactos=0
    while True:
        op=menu()
        if op=="1":
            nr_contactos=Add(contactos,nr_contactos)
        elif op=="2":
            pass
        elif op=="3":
            pass
        elif op=="4":
            pass
        elif op=="5":
            break
        else:
            print("Opção não é válida!")

if __name__=="__main__":
    main()
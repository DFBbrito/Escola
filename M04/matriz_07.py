"""
Fazer um programa para gerir os contactos de uma agenda. 
Deve permitir adicionar nome e telefone de cada contacto. 
Deve permitir listar todos e pesquisar por um nome.
Deve permitir Alterar o telefone de um nome.
"""
import numpy as np

def NomeRepetido(contactos,nr_contactos,nome):
    for i in range(nr_contactos):
        if nome==contactos[i,0]:
            return True    
    return False
    
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
    if nr_contactos==contactos.shape[0]:
        print("A agenda está completa")
        return
    nome=input('Digite o nome novo contacto:')
    numero=input("Digite o numerodo novo contacto:")
    #guardar na matriz
    contactos[nr_contactos,0]=nome
    contactos[nr_contactos,1]=numero
    nr_contactos+=1
    #devolve o nr de contactos
    return nr_contactos

#funçao para adicionar novo contacto por ordem alfabética e devolve o nr de contactos
def Add_v2(contactos,nr_contactos):
    if nr_contactos==contactos.shape[0]:
        print("A agenda está completa")
        return
    nome=input('Digite o nome novo contacto:')
    if NomeRepetido(contactos,nr_contactos,nome):
        print("Nome já existe na agenda!")
        return
    numero=input("Digite o numerodo novo contacto:")
    #procurar a linha onde inserir o novo contacto
    if nr_contactos==0:        
        #guardar na matriz
        contactos[nr_contactos,0]=nome
        contactos[nr_contactos,1]=numero
        nr_contactos+=1
        #devolve o nr de contactos
        return nr_contactos
    else:
        for l in range(nr_contactos):
            if nome<contactos[l,0]:
                #criar os restantes uma posiçao para a frente
                for posiçao in range(nr_contactos,l,-1):
                    contactos[posiçao,0]=contactos[posiçao-1,0]
                    contactos[posiçao,1]=contactos[posiçao-1,1]
                contactos[l,0]=nome
                contactos[l,1]=numero
                nr_contactos+=1
                return nr_contactos
        #inserir no final
        contactos[nr_contactos,0]=nome
        contactos[nr_contactos,1]=numero
        nr_contactos+=1
        #devolve o nr de contactos
        return nr_contactos
    
def Listar(contactos,nr_contactos):
    for l in range(nr_contactos):
        print(f"Nome:{contactos[l,0]} - Telefone: {contactos[l,1]}")

#mostra o nº de um ou vários contactos com base em parte do nome
def Pesquisa(contactos,nr_contactos):
    nome=input("Nome a pesquisar: ")
    encontrei=False
    for i in range(nr_contactos):
        if nome in contactos[i,0]:
            print(f'Nome:{contactos[i,0]} - Telefone: {contactos[i,1]}')
            encontrei=True
    if encontrei==False:
        print(f"Não existe nenhum contacto com o nome {nome}")

#Editar um contacto
def Alterar(contactos,nr_contactos):
    nome=input('Qual o nome do contacto que quer alterar:')
    encontrei=False
    for i in range(nr_contactos):
        if nome in contactos[i,0]:
            print(f"Nome:{contactos[i,0]} - Telefone{contactos[i,1]}")
            encontrei=True
            #editar
            op = input("é este o contacto a editar (s/n)?")
            if op in "sS":
                novo_nome=input("Introduza o novo nome ou deixe em branco:")
                novo_numero=input("Introduza o novo numero ou deixe em branco:")
                if novo_nome!="":
                    contactos[i,0]=novo_nome
                if novo_numero!="":
                    contactos[i,1]=novo_numero
                return
    if encontrei==False:
        print(f'Nao existe nenhum com o nome {nome}')

def main():
    #matriz vai ter 100 linhas e 2 colunas
    FORMA=(100,2)
    contactos=np.empty(FORMA,'U50') #strings com 50 letras cada no máximo
    nr_contactos=0
    while True:
        op=menu()
        if op=="1":
            nr_contactos=Add_v2(contactos,nr_contactos)
        elif op=="2":
            Listar(contactos,nr_contactos)
        elif op=="3":
            Pesquisa(contactos,nr_contactos)
        elif op=="4":
            Alterar(contactos,nr_contactos)
        elif op=="5":
            break
        else:
            print("Opção não é válida!")

if __name__=="__main__":
    main()
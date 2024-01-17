#Daniel Brito
"""
o sr joaquim tem um restaurante com 6 mesas de 4 lugares cada.
Vamos fazer um programa para:
1.Entrada de Clientes-deve perguntar qual a mesa e quantas pessoas
2.Saida de clientes-deve perguntar qual a mesa
3.Listar mesas(listar as mesas livres e ocupadas)
4.terminar.deve pedir para confirmar
versao hacker:
O SR.Joaquim deve poder inserir o nº de mesas e a lotaçao de cada mesa
"""
import numpy as np 

NR_MESAS=6

mesas=np.empty(NR_MESAS,'i')

def menu():
    print("1.entrada de clientes")
    print('2.Saida de clientes')
    print('3.Lista das mesas')
    print('4.Terminar')
    opçao=input(':')
    return opçao

def Entrada(mesas):
    #TODO: verificar se já não exitem mesas disponiveis
    while True:
        #perguntar qual a mesa
        nr_mesas=int(input("Qual a mesa [1-6]?"))-1
        #verificar se nr da mesa é válido
        if nr_mesas<0 or nr_mesas>len(mesas)-1:
            print("Nº da mesa não é valido")
            continue
        #verififcar se a mesa está ocupada
        if mesas[nr_mesas]!=0:
            print("Essa mesa está ocupada")
        else:
            break
    #perguntar quantas pessoas
    while True:
        nr_pessoas=int(input("Quantas pessoas:"))
        if nr_pessoas<=0 or nr_pessoas>4:
            print('Nº de pessoas não é válido')
        else:
            break
    #registar a entrada
    mesas[nr_mesas]=nr_pessoas
    print(f"Pode-se sentar na mesa {nr_mesas+1}")

def Saida(mesas):
    #TODO:Verificar se exite pelo menos uma mesa ocupada
    #perguntar a mesa
    while True:
        nr_mesa=int(input("Qual foi a mesa que sairam:"))-1
        #verificar se nr da mesa é válido
        if nr_mesa<0 or nr_mesa>len(mesas)-1:
            print("Nº da mesa não é valido")
            continue
        if mesas[nr_mesa]==0:
            print("Mesa está vazia")
        else:
            break
    #registar a saida
    mesas[nr_mesa]=0
    print("Obrigado por visitar o nosso restaurante")

def Listar(mesas):
    #listar as mesas livres
    print("Lista de mesas livres")
    soma=0
    for m in range(len(mesas)):
        soma=soma+mesas[m]
        if mesas[m]==0:
            print(m+1)
    #listar as mesas ocupadas
    print("Lista de mesas ocupadas")
    for m in range(len(mesas)):
        if mesas[m]!=0:
            print(m+1)
    #listar o nr de clientes
    print(f'tem {soma} clientes no restaurante')

def main():
    NR_MESAS=6
    mesas=np.zeros(NR_MESAS,'i')
    #menu
    while True:
        op=menu()
        if op=="1":
            Entrada(mesas)
        elif op=="2":
            Saida(mesas)
        elif op=="3":
            Listar(mesas)
        elif op=="4":
            break
        else:
            print("Opção não é válida!")


if __name__=="__main__":
    main()
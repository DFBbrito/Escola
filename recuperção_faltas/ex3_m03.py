"""
Criar um programa que implementa as operações aritméticas básicas utilizando funções. 
Cada função deve receber dois parâmetros com os valores e mostrar o resultado da respetiva operação. 
"""
def soma(n1,n2):
    resultado=n1+n2
    print(f'Soma: {n1} + {n2} = {resultado}')

def subtraçao(n1,n2):
    resultado=n1-n2
    print(f'Subtraçao: {n1} - {n2} = {resultado}')

def multiplicar(n1,n2):
    resultado=n1*n2
    print(f'Multiplicação: {n1} x {n2} = {resultado}')

def divisao(n1,n2):
    resultado=n1/n2
    print(f'Divisão: {n1} / {n2} = {resultado}')

def menu():
    print('1.somar \n2.subtrair \n3.multiplicar \n4.dividir')
    op=input('escolha uma opção: ')
    x=float(input('Um valor: '))
    y=float(input('Outro valor: '))
    if op=='1':
        soma(x,y)
    elif op=='2':
        subtraçao(x,y)
    elif op=='3':
        multiplicar(x,y)
    elif op=='4':
        divisao(x,y)

def main():
    menu()

if __name__ == '__main__':
    main()
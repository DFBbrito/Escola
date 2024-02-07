"""
Criar um programa que implementa as operações aritméticas básicas utilizando funções. 
Cada função deve receber dois parâmetros com os valores e mostrar o resultado da respetiva operação. 
"""
def soma(n1, n2):
    resultado = n1 + n2
    print(f'Soma: {n1} + {n2} = {resultado}')

def subtracao(n1, n2):
    resultado = n1 - n2
    print(f'Subtração: {n1} - {n2} = {resultado}')

def multiplicar(n1, n2):
    resultado = n1 * n2
    print(f'Multiplicação: {n1} x {n2} = {resultado}')

def divisao(n1, n2):
    if n2 != 0:
        resultado = n1 / n2
        print(f'Divisão: {n1} / {n2} = {resultado}')
    else:
        print("Erro: Divisão por zero!")

def menu():
    print('1. Somar\n2. Subtrair\n3. Multiplicar\n4. Dividir')
    op = input('Escolha uma opção: ')
    x = float(input('Digite o primeiro valor: '))
    y = float(input('Digite o segundo valor: '))
    if op == '1':
        soma(x, y)
    elif op == '2':
        subtracao(x, y)
    elif op == '3':
        multiplicar(x, y)
    elif op == '4':
        divisao(x, y)
    else:
        print("Opção inválida!")

def main():
    menu()

if __name__ == '__main__':
    main()

#Daniel Brito
"""
Calculadora: apresentar um menu com 4 opçoes
"""
def soma(n1,n2):
    resultado=n1+n2
    print(f'Soma: {resultado}')

def subtraçao(n1,n2):
    resultado=n1-n2
    print(f'Subtraçao: {resultado}')

def multiplicar(n1,n2):
    resultado=n1*n2
    print(f'Multiplicação: {resultado}')

def divisao(n1,n2):
    resultado=n1/n2
    print(f'Divisão: {resultado}')

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
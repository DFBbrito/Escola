#Daniel Brito
"""
Calculadora: apresentar um menu com 4 opçoes
"""
def soma(n1,n2):
    resultado=n1+n2
    return resultado

def subtraçao(n1,n2):
    resultado=n1-n2
    return resultado

def multiplicar(n1,n2):
    resultado=n1*n2
    return resultado

def divisao(n1,n2):
    resultado=n1/n2
    return resultado

def menu():
    while True:
        print('1.somar \n2.subtrair \n3.multiplicar \n4.dividir \n5.sair')
        op=input('escolha uma opção: ')
        if op=='5':
            break
        x=float(input('Um valor: '))
        y=float(input('Outro valor: '))
        if op=='1':
            r=soma(x,y)
        elif op=='2':
            r=subtraçao(x,y)
        elif op=='3':
            r=multiplicar(x,y)
        elif op=='4':
            r=divisao(x,y)
        print(r)

def main():
    menu()

if __name__ == '__main__':
    main()
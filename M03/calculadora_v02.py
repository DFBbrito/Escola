#Daniel Brito
"""
Calculadora: apresentar um menu com 4 opçoes
"""

print('1. Soma')
print('2. Subtrair')
print('3. Multiplicar')
print('4. dividir')

resposta= input('Escolha uma opção:')

def soma(x,y):
    A=x+y
    print(f'Soma {A}')

soma(10,5)
"""
Daniel Brito
"""
x = -1
while x<0:
    x = int(input("Digite um valor numerico inteiro: "))
    if x<0:
        print("O numero nao é valido. Digite outro numero inteiro positivo")

if x % 2 == 0:
    print("O numero é par.")
else:
    print("O numero é impar.")

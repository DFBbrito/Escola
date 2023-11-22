#Daniel Brito#
"""
Série de Fibonacci até N: Escreva um programa que imprime a série de Fibonacci até um número N 
fornecido pelo usuário. 
Lembre-se de que a série de Fibonacci é uma sequência onde cada número é a soma dos dois anteriores, 
começando com 0 e 1.
"""

N=int(input("Quantos nº pretende para definir o limite? "))
print("0\n1")
before1=0
before2=1
for o in range(N-2):
    numero= before1+before2
    print(numero)
    before1=before2
    before2=numero
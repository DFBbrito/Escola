#Daniel Brito#
"""
Problema 2
"""
nr_pessoas=int(input('Quantas pessoas: '))
soma_alturas=0
maior_altura=0
for i in range(nr_pessoas):
    altura = float(input(f"Qual a altura da {i+1}ª pessoa: "))
    #Calcular a soma total para depois fazer a média
    soma_alturas += altura
    if altura>maior_altura:
        maior_altura=altura
media=soma_alturas/nr_pessoas
print("A maior altura é %.1f e a média é %.1f"%(maior_altura,media))


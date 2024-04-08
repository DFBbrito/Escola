#Daniel Brito#
"""
Problema 2
"""
n_pessoas = int(input("Quantas pessoas são?"))
soma = 0
for _ in range(n_pessoas):
    altura= float(input("Quanto mede a pessoa? "))
    maior = altura%n_pessoas
    soma = soma + altura
    
media= soma/n_pessoas
print(f'A maior altura é {maior}')
print(f"A média é:{media}")
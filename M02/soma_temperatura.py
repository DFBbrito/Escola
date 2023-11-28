"""
feito em IA (bing.com)
"""
soma_temperaturas = 0
maior_temperatura = -float('inf')
menor_temperatura = float('inf')
i = 0
contar_negativas = 0
contar_positivas = 0

#for i in range(1,6)
while i < 5:
    temperatura = float(input(f'Insira a temperatura {i+1}: '))
    soma_temperaturas += temperatura
    #verificar se é a maior temp
    if temperatura > maior_temperatura:
        maior_temperatura = temperatura
    #verificar se é a menor temp
    if temperatura < menor_temperatura:
        menor_temperatura = temperatura
    #contar se a temp é negativa  
    if temperatura>0:
        contar_negativas += 1
    #contar se a temp é positva
    if temperatura<0:
        contar_positivas += 1
    i = i + 1

media_temperaturas = soma_temperaturas / 5

print(f'A média das temperaturas é: {media_temperaturas}')
print(f'A maior temperatura é: {maior_temperatura}')
print(f'A menor temperatura é: {menor_temperatura}')
print(f'Temperaturas negativas: {contar_negativas}')
print(f'Temperaturas positivas: {contar_positivas}')

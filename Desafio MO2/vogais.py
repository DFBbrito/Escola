"""
Daniel Brito
"""
vogais = 'aeiouAEIOU' #string a contar vogais
contagem_vogais = 0

for i in range(10):
    letra = input("Digite a %d letra: "%(i +1))
    if letra in vogais:
        contagem_vogais += 1
print("Voçe introduziu %d vogais"%(contagem_vogais))


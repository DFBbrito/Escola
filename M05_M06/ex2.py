notas=[10,5,15,10]

#Media
Media=sum(notas)/len(notas)

#Media v2
for x in notas:
    soma=soma+x
    #mostrar nota
    print(x)
media=soma/len(notas)

#mostrar media
print(f"{media=}")

#percentagem de nagativas
negativas=0
for x in notas:
    if x<10:
        negativas+=1

perc_negativas=negativas/len(notas)*100
perc_positivas=100-perc_negativas
perc_negativas=negativas/len(notas)*100
print(f"{perc_negativas=}{perc_positivas=}")

#melhor nota
melhor=notas[0]
for x in notas:
    if x>melhor:
        melhor=x
print(f"{melhor=}")

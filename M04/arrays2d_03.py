"""
Um programa para ler do utilizador as temperaturas mensais de 3 cidades.
O programa deve mostrar a temperatura mais elevada.
Hacker:
    Calcular a média das temperaturas por cidade
    Calcular a média das temperaturas por mês
    Mostrar a cidade com a temperatura média mais elevada
    Mostrar o mês com a temperatura média mais elevada
"""
#declarar um array de 2 dimensões com 3 linhas e 12 colunas
import numpy as np


#array com 3 linhas e 12 colunas
MAX_ITEMS=(3,12)
temperaturas=np.zeros(MAX_ITEMS)
cidades=np.array(["Viseu","Coimbra","Lisboa"])

#ler as temperaturas
#ciclo para percorrer as linhas (Cidades)
for l in range(temperaturas.shape[0]):
    #ciclo para as colunas (meses)
    for c in range(temperaturas.shape[1]):
        temp=float(input(f'Introduza a temperatura para a cidade {cidades[l+1]} correspondente ao mês {c+1}: '))
        #guardar no array
        temperaturas[l,c]=temp
        
#Procurar a temperatura mais elevada
#guardar a primeira temperatura como sendo a maior
maior_temp=temperaturas[0,0]
#percorrer o array
for l in range(temperaturas.shape[0]):
    for c in range(temperaturas.shape[1]):
        if temperaturas[l,c]>maior_temp:
            maior_temp=temperaturas[l,c]
print(f"A maior temperatura foi {maior_temp}")

#Calcular a média das temperaturas por cidade
for l in range(temperaturas.shape[0]):
    soma=0
    for c in range(temperaturas.shape[1]):
        soma+=temperaturas[l,c]
    media=soma/12
    if l==0 or media>maior_media:
        maior_media=media
        cidade=l
    #elif media>maior_media:
     #   maior_media=media
      #  cidade=l        
    print(f'A média da temperatura da cidade {l+1} foi {media:.1f}')
#Mostrar a cidade com a temperatura média mais elevada
print(f'A cidade com a temperatura média mais elevada foi {cidade+1}')


#Calcular a média das temperaturas por mês
for c in range(temperaturas.shape[1]):
    soma=0
    for l in range(temperaturas.shape[0]):
        soma+=temperaturas[l,c]
    media=soma/3
    if c==0 or media>maior_media:
        maior_media=media
        mes=c
    #elif media>maior_media:
     #   maior_media=media
      #  cidade=l        
    print(f'A média da temperatura do mês {c+1} foi {media:.1f}')
#Mostrar o mês com a temperatura média mais elevada
print(f'O mês com a temperatura média mais elevada foi {mes+1}')

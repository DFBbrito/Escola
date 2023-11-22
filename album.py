#Daniel Brito#
"""
Um programa para calcular a duração total de um album. Para isso é necessário inserir a duração de cada música. A duração de cada música é inserida em segundos, mas a duração total deve ser mostrada em minutos:segundos
a) Pedir quantas músicas primeiro
b) Ler até inserir duração 0 (zero)
"""

n_music = int(input('Quantas musicas sao?'))
duraçao_total= 0
for i in range(n_music):
    duraçao_music = int(input('Se quiseres terminar digita(0). Insira as musicas em segundo: '))
    #verificar
    if duraçao_music == 0:
        break
    #adicionar a duraçao a duraçao total
    duraçao_total += duraçao_music

#calcular minutos e segundos
m = int(duraçao_total/60)
s = duraçao_total-m*60

print(f'A duraçao total é: {m}:{s}')

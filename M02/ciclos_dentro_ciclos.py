"""
Um programa que mostre os nº de 1 a 10 e depois os nº de 10 a 1 e repita 5x
"""
#Daniel Brito#

#repetir 5x
for n in range(5):
    #crescente
    for i in range(1,11):
        print(i)
    #decrescente
    for m in range(10,0,-1):
        print(m)

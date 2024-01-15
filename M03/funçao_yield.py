def gerar_pares(limites):
    n=0
    while n<=limites:
        yield n
        n+=2

for numero_par in gerar_pares(10):
    print(numero_par)

#def range_pt(limite,inicio=0,passo=1):
#    n=inicio
#    while n < limite:
#        yield n 
#        n+=passo

#for n in range_pt(10,2,2):
#    print(n)
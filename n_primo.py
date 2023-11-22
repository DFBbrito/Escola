#ler o nº do utilizador
n = int(input("Digite um numero:"))
#variavel para contar divisores
nd = 0
#percorrer todos os nº ate 1
for i in range(n,0,-1):
    #testar se i é divisivel n
    if n%2 ==0:
        nd = nd + 1
        print("%d é divisor"%i)
        if i!=n and i!=1:
            nd=3
            break
#se tiver só 2 divisores é primo
if nd==2:
    print("%d é primo"%n)
else:
    print("%d não é primo"%n)


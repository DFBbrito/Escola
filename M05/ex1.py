lista=[]

#for i in range(5):
#   x=int(input("Valor:"))
#   lista.append(x)

#
while True:
    numeros=input("Insira 5 numeros separados por espaços em branco:")
    temp=numeros.split()
    if len(temp)>=5:
        break

lista=[int(x) for x in temp]

lista=lista[0:5]
#

for x in lista:
    print(x)

soma=sum(lista)
media=soma/len(lista)
print(f"media {media:.2f}")


"""
Daniel Brito
"""
#Grupo 1 
#1 
n1=int(input("Diga um numero: "))
n2=int(input("Diga um numero: "))

if n1==n2:
    print('Iguais')
elif n1!=n2:
    print("Diferença")

#2
n1=float(input("Diga um numeor:"))
n2=float(input("Diga um numeor:"))
n3=float(input("Diga um numeor:"))

if n1>n2 and n1>n3:
    print(n1,'É o maior')
if n1>n2 and n1>n3:
    print(n1,'É o maior')
if n1>n2 and n1>n3:
    print(n1,'É o maior')

#Grupo 2
#1 
for i in range(10):
    print("33")

#2
while True:
    n1=int('Diga um numero:')
    if n1>0:
        print("Positivo")
    elif n1<0:
        print("Negativo")
    if n1==0:
        break

#3
soma=0
for i in range(5):
    n=float(input("Diga um numero:"))
    soma+=n

media=soma/5
print("A media é", media)
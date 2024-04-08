#Igualdade em listas
l1=[1,2,3,4]
l2=[1,2,3,4]
l3=[4,3,2,1]

print(l1==l2)

print(l1==l3) #diferentes porque ordem interessa

l4=l1
l4.append(5)  #adiciona
print(l1==l4)

t=(1,2,3,4)
print(l2==t)

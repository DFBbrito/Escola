#igualdade em tuplos
t1=(1,2,3,4)
t2=(1,2,3,4)
t3=(4,2,3,1)

print(t1==t2)
print(t1==t3) #diferentes por causa de ordem

t4=t1
t4=(1,2) #cria um tuplo novo
print(t1==t4)
print(t1)
print(t4)
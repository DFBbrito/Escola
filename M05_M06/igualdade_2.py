#Igualdade em sets
conjunto_1={1,2,3,4,5}
conjunto_2={1,2,3,4,5}
conjunto_3={5,2,3,4,1}
conjunto_4={1,2,3,4,6}

print(conjunto_1==conjunto_2) #igual porque a ordem ñ interessa
print(conjunto_1==conjunto_3) 
print(conjunto_2==conjunto_3)
print(conjunto_1==conjunto_4)
print(conjunto_2==conjunto_4)
print(conjunto_3==conjunto_4)

novo=conjunto_1
novo={4,5,6,7,8}
print(novo==conjunto_1)


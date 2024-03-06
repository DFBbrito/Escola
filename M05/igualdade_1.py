#Igualdade de dicionarios
d1={"carro":"ford","preco":10000}
d2={"preco":10000,"carro":"ford"}
d3={"carro":"vw","preco":10000}
d4={"carro":"ford","preco":10000,"ano":2019}

print(d1==d2)   #iguais porque a ordem ñ interessa
print(d2==d3)
print(d3==d4)
print(d1==d3)
print(d1==d4)
print(d2==d4)

d=d1
d["modelo"]="fiesta"
print(d==d1)
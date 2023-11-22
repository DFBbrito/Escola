base = int(input("Qual a base: "))
expoente = int(input("Qual o expoente: "))

produto=1

for i in range(expoente):
    produto = produto * base
print(produto)


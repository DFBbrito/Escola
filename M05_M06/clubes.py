def LerNomes(lista):
    while True:
        nome=input("nome:")
        if nome:
            lista.append(nome)
        else:
            break

clube1=[]
clube2=[]

print("Nomes do clube 1")
LerNomes(clube1)
print("Nomes do clube 2")
LerNomes(clube2)

#lista com nomes repetidos
repetidos=[]
for nome in clube1:
    if nome in clube2:
        repetidos.append(nome)

for nome in repetidos:
    op=input(f"{nome} quer o clube 1 ou clube 2:")
    if op=="1":
        clube2.remove(nome)
    else:
        clube1.remove(nome)

#ordenar as listas
clube1.sort()
clube2.sort()
repetidos.sort()
print(f"Clube1:{clube1},Clube2:{clube2} e repetidos:{repetidos}")
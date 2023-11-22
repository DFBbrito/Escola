texto = (input("Introduza o seu nome: "))
contar = 0 

for letra in texto:
    print(letra)
    if letra==" ":
        contar= contar + 1 
print("tem %d palavras"%(contar + 1))

contar_vogais = 0 
for letra in texto:
    if letra in "aeiouAEIOU":
        contar_vogais += 1
print("tem %d vogais"%contar_vogais)


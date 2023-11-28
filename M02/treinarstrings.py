"""
Pedir ao utilizador uma frase e mostrar
a 1º letra em maiuscula de cada palavra


"""

frase = (input("Digite a frase: "))
frase = frase.strip()
frase2 = frase[0].capitalize()
for i in range(len(frase)-1):
    if frase[i]==" ":
        frase2=frase2+frase[i+1].capitalize()
    else:
        frase2=frase2+frase[i+1].lower()

print(frase2)

from string import punctuation

x = input("Digite qualquer coisa: ")

for i in range(len(x)-1):
    if x[i].isalpha():
        print("Alfabeto")
    if x[i].isdigit():
        print("Digito")
    if x[i].isspace():
        print("Espaço")
    if x[i] in punctuation:
        print("Pontuaçao")

print(" ")



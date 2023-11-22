#ler palavra ou nº e dizer se a palavra for capicua
texto=input("texto a testar? ")
texto2 = ""

for i in range(len(texto)-1,-1,-1):
    texto2= texto2 + texto[i]
if texto==texto2:
    print("Capicua!")
else:
    print("Não é capicua!")

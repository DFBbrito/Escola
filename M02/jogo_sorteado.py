import random

numero_secreto=int(random.random()*10+1)

while True:
    tentativas= int(input("Quantas vezes queres tentar (1 a 5): "))
    if tentativas<1 or tentativas>5:
        print("Nº Invalido.")   
    else:
        break

while tentativas>0:
    print("Tem %d tentativas"%tentativas)
    valor= int(input("Diz me o numero que pensas? (1 a 10): "))
    if valor>10 or valor<0:
        print("O nº é inválido")
        continue
    #testar se acertou
    if valor == numero_secreto:
        print("Acertou!!")
        break
    if tentativas>1:
        if numero_secreto > valor:
            print("O nº secreto é superior")
        else:
            print("O nº secreto é menor")
    tentativas = tentativas - 1 
else:
    print("O numero secreto era %d"%numero_secreto)



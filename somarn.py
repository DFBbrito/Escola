#precisamos somar n valores  inseridos pelo utilizador 

n = int(input("Quantos valores pretende inserir:"))
soma=0
for i in range(n):
    x= int(input("Introduza um valor:"))
    soma = soma + x
    # verificar se é o primeiro valor 
    if i==0:
        maior = x #se é o primeiro este é o valor (não há outro )
    elif x > maior:
        maior = x #o novo nº é maior 


print("A soma é %d"%soma)
print("Média %.2f"%(soma/n))
print("O maior valor introduzido foi %d"%maior) 

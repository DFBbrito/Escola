#Daniel Brito#
"""
Você está fazendo compras em um supermercado com um orçamento e uma capacidade de peso limitados.
Seu objetivo é maximizar o número de itens que você pode comprar sem exceder seu orçamento e a capacidade de peso 
que você pode levar.
De cada vez que adicionar um produto à lista de compras deve indicar quanto dinheiro ainda sobre e quanto peso
ainda pode carregar.
"""

#orçamento
valor = float(input("Quanto dinheiro deseja gastar(€)? "))
#capacidade de peso que pode levar
peso = float(input('Quantidade em peso?(kg) '))

valor_total = 0
peso_total= 0

#quando adiciona produto a lista deve indicar o dinheiro sobra e peso que resta
while True:
    produto_preço = float(input("Quanto custa o produto(€): "))
    produto_peso = float(input("Quanto pesa o produto(kg): "))
    
    if produto_preço<0 or produto_peso<0:
        print("valores do porduto invalidos. Programa a encerrar.")
        break
    
    if valor - produto_preço < 0:
        print("Excedeu o orçamento.")
        print(f"poderia levar mais {peso}kg")
    elif peso - produto_peso < 0:
        print("Excedeu a capacidade de peso.")
        print(f'ficou com {valor}€')
        break

    valor -= produto_preço
    peso -= produto_peso
    valor_total += valor
    peso_total += peso

    print(f'Resta lhe {valor:.2f}€ e resta lhe {peso:.2f}kg')

    if peso==0:
        print('O seu peso maximo foi exedido, nao pode levar mais produtos')
        continuar = input('se deseja continuar digite S, se deseja terminar digite N: ')
        if continuar.upper() != "S":
            break
       
    if valor==0:
        print('O seu orcamento foi ultrapassado, nao pode comprar mais produtos')
        continuar = input('se deseja continuar digite S, se deseja terminar digite N: ')
        if continuar.upper() != "S":
          break
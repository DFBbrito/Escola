"""
    Menu
1 -  Carregar 
2 - Descarregar 
3 - Sair

limite : 10000 Kg
Carga:
"""
#Daniel Brito#
peso_atual = 0

while True:
    print(f"Peso atual {peso_atual}. Disponibilidade: {10000-peso_atual}. ")
    print("1. Carregar\n2. Descarregar\n3. Sair\n")
    opçao = input("Escolha uma opçao: ")
    #se escolher sair
    if opçao == "3":
        break
    #se escolher carregar 
    if opçao == "1":
        #qual o peso da carga
        carga = int(input("Quanto deseja carregar? "))
        if carga<=0:
            print("Valor Inválido")
            continue
        peso_atual += carga
        if peso_atual > 10000:
            print("Peso máximo excedido.")
            peso_atual -= carga


    #se escolher descarregar
    if opçao == "2":
        carga = int(input("Quanto deseja descarregar? "))
        if carga<0:
            print("Valor inválido")
            continue
        peso_atual -= carga
        if peso_atual < 0:
            print("Valor de carga não existe.")
            peso_atual += carga


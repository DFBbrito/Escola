#precisamos de um programa para gerir a lotaçao de um restaurante que tem 100 lugares
#de cada vez que chegam clientes é intruduzido o nº de pessoas a sentar
#se esse nº for 0 (zero) o programa termina
#se nº for >0 devemos indicar quantos lugares sobram, depois dessas pessoas se sentarem ou se ja nao ha lugares para eles
#hacker: Ter em conta que o restaurante só tem 20 mesas, e que cada vez que entram clientes é ocupada uma mesa  

n_lugares = 100
mesas=20

#ciclo infinito
while True:
    #ler quantas pessoas querem entrar
    n_pessoas= int(input("Pessoas para entrar: "))
    #testar se devemos terminar o o programa
    if n_pessoas == 0:
        break
    #testar se temos lugares disponiveis
    if n_lugares>=n_pessoas and mesas>0:
        #atualizar o nº de lugares livres   
        n_lugares= n_lugares - n_pessoas
        #atualizar o nº de mesas 
        mesas = mesas - 1
        print("tem ",n_lugares,"livres e ",mesas,"mesas")
    else:
        print("não tem tantos lugares disponiveis. So tem",n_lugares,"e",mesas,"mesas")


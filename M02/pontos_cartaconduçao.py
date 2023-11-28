#Daniel Brito#
"""
Em Portugal, o sistema de pontos na carta de condução foi implementado para promover uma condução mais segura e 
responsável. Cada condutor começa com um total de 12 pontos, que podem ser perdidos em função das infrações 
cometidas. A quantidade de pontos perdidos depende da gravidade da infração.

Infrações muito graves: resultam na perda de 6 pontos. 
Infrações graves: Estas infrações levam à perda de 4 pontos.
Infrações leves: Não perde pontos caso seja a primeira infração deste tipo, ou perde 1 ponto nas restantes vezes.
Duas infrações graves ou uma infração grave e uma muito grave levam à perda da carta durante 1 ano.
O condutor também perde a carta quando fica com 0 (zero) pontos.

Faça um programa em que o utilizador insere o número e tipo de infraçãooes que cometeu e o programa vai mostrando 
os pontos restantes da carta e se perde ou não a carta.
O programa deve apresentar um menu com as opções correspondentes ao tipo de infrações e outra opção para terminar.

Por exemplo:
Tem 12 pontos restantes
Escolha uma opção:
1. Infração muito grave
2. Infração grave
3. Infração leve
4. Terminar
"""

pontos = 12
inf_muito_grave = 6
inf_grave = 4
inf_leve_primeira = 0
inf_leve_repetida = 1

for _ in range(3):
    print(f'Tem {pontos} pontos restantes')
    print('Escolha uma opçao: ')
    print("1. Infraçao muito grave")
    print("2. infraçao grave")
    print("3. infraçao leve")
    print("4. terminar")

    escolha=input("Opçao: ")

    if escolha == "1":
        pontos -= inf_muito_grave
    elif escolha == "2":
        pontos -= inf_grave
    elif escolha == "3":
        if inf_leve_primeira > 0:
            print('Infração leve nao perde pongtos (primera vez).')
            inf_leve_primeira += 1
        else:
            pontos -= inf_leve_repetida
    elif escolha == "4":
        break
    else:
        print('Opcao inválida!')

    if pontos <= 0:
        print('Perdeu a carta!')
        break

    if pontos <= 2:
        print('Atençao: ficou com menos de 3 pontos na carta de conduçao. (nao pode cometer infrações)')
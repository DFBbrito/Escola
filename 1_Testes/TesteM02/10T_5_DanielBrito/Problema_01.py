#Daniel Brito#
"""
Problema 1
"""

estrada = input('Qual a estrada? ')
consumo = int(input('Consumo de combustivel do seu veiculo (litros totais consumidos): '))
classe_veiculo = input('Qual a classe do veiculo? ')

custo_total = 0

while True:
    if estrada == "A1":
        custo_total = 1.9*consumo
        if classe_veiculo == "A":
            custo_total = custo_total + 6.52
        elif classe_veiculo == "B":
            custo_total = custo_total + (6.52+0.2)
        elif classe_veiculo == "C":
            custo_total = custo_total + (6.52+0.4)
        print(f'O custo da viagem é {custo_total}€')
        break
    elif estrada == "A20":
        custo_total = 1.8*consumo
        if classe_veiculo == "A":
            custo_total = custo_total + 15.2
        elif classe_veiculo == "B":
            custo_total =custo_total + (15.2+0.2)
        elif classe_veiculo == "C":
            custo_total = custo_total + (15.2+0.4)
        print(f'O custo da viagem é {custo_total}€')
        break
    elif estrada == "A21":
        custo_total = 1.75*consumo
        if classe_veiculo == "A":
            custo_total = custo_total + 5.75
        elif classe_veiculo == "B":
            custo_total =custo_total + (5.75+0.2)
        elif classe_veiculo == "C":
            custo_total = custo_total + (5.75+0.4)
        print(f'O custo da viagem é {custo_total}€')
        break
    
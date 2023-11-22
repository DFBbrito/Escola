"""
problema 1
"""
#Dados de entrada
estrada =  input("Estrada: ")
classe = input("Classe: ")
consumo_no_total = int(input("Consumo total: "))

if estrada=="A1":
    portangens = 6.52
    custoLitro = 1.9
elif estrada=="A20":
    portangens=15.2
    custoLitro=1.8
else:
    portangens=5.75
    custoLitro=1.75

if classe=="B":
    portangens=portangens*1.2
elif classe=="C":
    portangens=portangens*1.4

custo=consumo_no_total*custoLitro+portangens
print(f'A viagem fica em {custo}€')


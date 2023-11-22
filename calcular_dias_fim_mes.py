#Daniel Brito#
"""
Calcular quantos dias faltam para o fim do mês

Dados: dia e o mês atual
"""

#validaçao dos dados
while True:
    mês = int(input('qual o mês: '))
    #validar o mês
    if mês<1 or mês>12:
        print('O valor do mês deve estar entre 1 e 12')
    else:
        break

while True:
    dia = int(input('qual o dia: '))
    #meses com 31 dias
    if mês in (1,3,5,7,8,10,12):
        restante = 31 - dia
    elif mês == 2:
        restante = 28 - dia
    else:
        restante = 30 - dia 

    #validar o dia
    if  restante<0 or dia<1:
        print('O dia indicado não é válido')
    else:
        break

print(f'Falta {restante} dias para o fim do mês')


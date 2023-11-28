#Daniel Brito#
"""
calcular a idade da pessoa

Dados: dia, mês e ano de nacsimento
"""
import datetime

dia = int(input('Qual o dia em que nasceu? '))
mes = int(input('Qual o mês em que nasceu? '))
ano = int(input('Qual o ano em que nasceu? '))

hoje = datetime.date.today()

ANO_ATUAL = hoje.year
MES_ATUAL = hoje.month
DIA_ATUAL = hoje.day

idade = ANO_ATUAL - ano

#verificar se ainda nao fez anos
if mes>MES_ATUAL or (mes==MES_ATUAL and dia>DIA_ATUAL):
    idade = idade - 1 

print(f'Tem {idade} anos')

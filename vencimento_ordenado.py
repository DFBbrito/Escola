#Daniel Brito#
"""
calcular vencimento do trabalhor, na base de vencimento por dia, e as datas quando começou a trabalhar
validar 
"""
import datetime

datetime.datetime.today()


#data que começou a trabalhar 
start = input("Quando começou a trabalhar:")
#data que terminou de trabalhar
finish = input("Quando é que terminou o trabalho:")

#validaçao

#Calcular quantos dias trabalhou 
start_d = datetime.datetime.strptime(start,"%d-%m-%Y") 
finish_d = datetime.datetime.strptime(finish,"%d-%m-%Y")
#calcular a diferença entre a data de termino e inico de trabalho
dias = finish_d - start_d


#Pedir ao utilizador quanto ganha por dia
earn = float(input("Quanto ganha:"))
#calcular vencimento
vencimento = dias.days * earn
print(f'Deve receber {vencimento}€ porque trabalho {dias.days} dias')
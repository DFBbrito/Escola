#Daniel Brito#
"""
Datas
"""
import datetime 

hoje = datetime.date.today()

print(hoje.year)
print(hoje.month)
print(hoje.day)

#horas
print(datetime.datetime.now())

#Só a hora
print(datetime.datetime.now().strftime('%H:%M:%S'))


#calcular diferença entre duas datas
data1='2000-01-01'
data2='2000-02-01'
#converter para objetos datetime
data1_obj= datetime.datetime.strptime(data1,'%Y-%m-%d')
data2_obj= datetime.datetime.strptime(data2,'%Y-%m-%d')

diferença = data2_obj - data1_obj

print(diferença.days)
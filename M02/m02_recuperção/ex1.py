"""
faça um programa em python que leia o tempo em segundos de uma chamda, o tipo de chamda e o local 
para onde foi deita e mostre na consola o valor a pagar. O preço é calculado ao minuto,
por exemplo se a chamada tiver a duraçao de 125 segundos deverão ser cobrados 3 minutos na tarifa 
correspondente ao tipo de chamada efetuada
"""

tipo=input('Tipo de chamada? ')
local=input('Onde foi efetuada a chamada? ')
duraçao=input('Quanto tempo durou á chamada? ')
duraçao=int(duraçao)
min=duraçao//60

if duraçao%60!=0:
    min=min+1
if tipo=="videos":
    print(min*1.272)
elif local=="EEE":
    print(min*0.234)
elif local=="RE":
    print(min*0.735)
elif local=="AA":
    print(min*0.762)
elif local=="AO":
    print(min*1.862)

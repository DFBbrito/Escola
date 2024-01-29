#Daniel Brito#
"""
Problema 3
"""
mesas_disponiveis=15
pessoas_por_mesa=8
max_pessoas=mesas_disponiveis*pessoas_por_mesa
total_pessoas=0

while True:
    n_pessoas=int(input('Quantas pessoas:'))
    #termina quando nao existem mais pessoas para entrar
    if n_pessoas==0:
        break
    #termina quando nao existem mais lugares
    if n_pessoas+total_pessoas>max_pessoas:
        break
    total_pessoas=total_pessoas+n_pessoas

#Mesas cheias
mesas_cheias=int(total_pessoas/pessoas_por_mesa)
print('Mesas ocupadas %d'%mesas_cheias)
#mesas parcialmente cheias
mesas_parc=0
pessoas_sobram=total_pessoas-(mesas_cheias*8)
if pessoas_sobram>0:
    mesas_parc=1
print('Mesas parcialmente ocupadas: %d com %d pessoas'%(mesas_parc,pessoas_sobram))
#mesas vazias
mesas_vazias=mesas_disponiveis-mesas_cheias-mesas_parc
print('Mesas vazias %d'%mesas_vazias)





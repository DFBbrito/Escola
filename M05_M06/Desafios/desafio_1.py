#Daniel Brito
'''
PSI - Módulo 5
Estruturas de dados Compostas
Operações com Sets
'''

# Lista de marcas
F1={'Mercedes','Red Bull','Ferrari','McLaren','Alpine','Alpha Tauri','Aston Martin','Williams','Alfa Romeo','Haas'}

WEC={'Toyota','Glickenhaus','Alpine','Peugeot','Ferrari','Porsche','Aston Martin'}


# União
print('--------------------------------------------------')
print('Todas as equipas que correm na F1 ou no WEC: ')
print('--------------------------------------------------')
uniao=F1.union(WEC)
print(uniao)


# Diferença
print('--------------------------------------------------')
print('Equipas que só competem na F1')
print('--------------------------------------------------')
diferença=F1.difference(WEC)
print(diferença)

# Interseção
print('-----------------------------------------')
print('Equipas que correm na F1 e no WEC:')
print('-----------------------------------------')
interseçao=F1.intersection(WEC)
print(interseçao)

# Diferença
print('------------------------------------------')
print('Equipas que só competem no WEC')
print('------------------------------------------')
diferença=WEC.difference(F1)
print(diferença)


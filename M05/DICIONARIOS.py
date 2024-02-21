###dicionarios###

dicionario={'Joaquim': 911911911 , 'Maria' : 123123123  , 'Jose' : 912912912}
print(dicionario['Maria'])

print("-----")

contactos={'Maria':(123123123,"maria@gmail."),'Joaquim': 123123}
print(contactos['Maria'][1])

print("------------------------")

chaves=dicionario.keys()

for chave in chaves:
    print(dicionario[chave])

print("-----")

valores=dicionario.values()

for valor in valores:
    print(valor)

print("-----")

for chave,valor in dicionario.items():
    print(f'O ñ: de {chave} é {valor}')

print("-")

print(dicionario)

dicionario['Galileu']=111222333

print(dicionario)

print("-")

n=dicionario.get('Joana','Não existe')
print(n)

print("-")

dicionario_A={'A':1,'B':2}
dicionario_B={'A':2,'B':3,'C':4}

dicionario_A.update(dicionario_B)

print("-")

x=dicionario_A.pop('A')

print(x)

print(dicionario_B)

print("-")

del dicionario_A

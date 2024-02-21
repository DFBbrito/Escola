paises={'Portugal':"Lisboa",'France':"Paris",'Inglaterra':"Londres",'Espanha':"Madrid"}

for chave,valor in paises.items():
    print(f"A capital de {chave} é {valor}!")


pais=input("diga um Pais: ")
capital=input("diga uma capital: ")

paises[pais]=capital

print(paises)

while True:
    questao=input("Quer saber o Pais ou a Capital? ")
    if questao == "Pais":
        questao=input#todo
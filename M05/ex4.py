signos=["rato","Búfalo","Tigre","Coelho","Dragão","Serpente","Cavalo","Cabra","Macaco","Galo","Cão","Porco"]

data_nascimento=input("data de nascimento (dd/mm/aaaa):")
ano=int(data_nascimento[6:])

posiçao=(ano-1900)%12

print(signos[posiçao])

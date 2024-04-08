import random

super_heroes=["Spider-Man","Iron Man","Captain Amercia","Thor","Hulk","Black Panther","Doctor Strange","Vision"]

super_vilains=["Magneto","Doctor Doom","Thanos","Loki","Galactus","Kingpin","Green Goblin","Venon"]

while len(super_heroes)>0:
    #Simular o combate entre um vilão e um herói
    heroi=random.choice(super_heroes)
    vilao=random.choice(super_vilains)
    print(f"{heroi} vs {vilao}")
    #Nao repetir
    super_heroes.remove(heroi)
    super_vilains.remove(vilao)
    #sortear quem ganha
    combate=[heroi,vilao]
    vencedor=random.choice(combate)
    print(f"Vencedor foi {vencedor}")
    x=input("enter - proximo comabte")
    print("x"*12)



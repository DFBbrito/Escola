#funçao que le um inteiro do utilizador
def le_numero(titulo):
    temp=input(titulo)
    while not temp.isnumeric():
        temp=input(titulo)
    return int(temp)

#funçao para mostrar um menu
#mostrar_menu("Menu Principal",["Livros","Leitores",...])
def mostrar_menu(titulo,opçoes):
    print("="*40)
    print(titulo)
    print("="*40)
    for i in range(len(opçoes)):
        print(f"{i+1}-{opçoes[i]}")
    print("="*40)

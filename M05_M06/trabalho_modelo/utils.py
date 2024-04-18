#funçao que le um inteiro do utilizador
def le_numero(titulo):
    temp=input(titulo)
    while not temp.isnumeric():
        temp=input(titulo)
    return int(temp)

#funçao para ler um texto com um numero minimo de letras
def le_texto(titulo,minimo=None):
    temp=input(titulo)
    while minimo is not None and len(temp)<minimo:
        temp=input(titulo)
    return temp

#funçao lê, valida e devolve um endereço do email
def le_email(titulo):
    email=le_texto(titulo)
    while True:
        email=le_texto(titulo)
        tem_arroba=False
        for c in email:
            if c=="@":
                tem_arroba=True
            if tem_arroba:
                if c==".":
                    return email

#funçao para mostrar um menu
#mostrar_menu("Menu Principal",["Livros","Leitores",...])
def mostrar_menu(titulo,opçoes):
    print("="*40)
    print(titulo)
    print("="*40)
    for i in range(len(opçoes)):
        print(f"{i+1}-{opçoes[i]}")
    print("="*40)

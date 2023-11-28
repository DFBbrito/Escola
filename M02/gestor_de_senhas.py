#Daniel Brito#
"""
Gestor de senhas 

"""

avaliaçao_numeros=0
avaliaçao_minusculas=0
avaliaçao_maiusculas=0
avaliaçao_especiais=0
senha = input('digite a senha a ser testada: ')
#se a senha tiver mesnos de 7 carateres é fraca
if len(senha)<7:
    print("Fraca")
else:
    for letra in senha:
        #se tem números
        if letra in "0123456789":
            avaliaçao_numeros=1
        #especiais
        if letra in "#&$£@%!?;:.-_=+*<>\\/^~{}()[]":
            avaliaçao_especiais=1
        #minusculas
        if ord(letra)>=97 and ord(letra)<=122:
            avaliaçao_minusculas=1
        #maiusculas
        if ord(letra)>=65 and ord(letra<=90):
            avaliaçao_maiusculas=1
        if avaliaçao_numeros==1 and avaliaçao_minusculas==1 and avaliaçao_maiusculas==1 and avaliaçao_especiais==1:
            break
    avaliaçao= avaliaçao_especiais+avaliaçao_maiusculas+avaliaçao_minusculas+avaliaçao_numeros
    #senha fraca
    if avaliaçao==1:
        print("Fraca")
    elif avaliaçao<=3:
        print("Média")
    else:
        print("Forte")
    

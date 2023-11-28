"""
Vamos fazer o jogo do enforcado
>>enforcado V0.5<<

"""
#Daniel Brito#

palavra = "banana"
palavra_j = "_"*len(palavra)
tentativas = 7


while tentativas>0:
    letra = input("letra: ").lower()
    temp = ""
    acertou = False
    for i in range(len(palavra)):
        if letra == palavra[i]:
            temp += letra
            acertou = True
        else:
            temp += palavra_j[i]
    palavra_j = temp
    #testar se nao acertou na letra
    if acertou == False:
        tentativas -= 1
    #testar se ganhou
    if palavra == palavra_j:
        print(f"Acertou na palavra: {palavra}")
        break
    print(palavra_j)
    print(f'tentativas restantes {tentativas}')
if tentativas==0:
    print(f'Errou a palavra, a palavra era {palavra}')

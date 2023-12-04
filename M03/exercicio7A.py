#Daniel Brito
"""
implemntar uma funçao que verifique se uma string é um palindromo.
"""
def Palindromo(palavra):
    invertida=""
    for letra in palavra:
        invertida=letra+invertida
    invertida=invertida.lower()
    palavra=palavra.lower()
    if palavra==invertida:
        print('é palindromo')
    else:
        print('ñ é palindromo')

def main():
    palavra=(input('Diga uma palavra: '))
    Palindromo(palavra)
    

if __name__ == "__main__":
    main()
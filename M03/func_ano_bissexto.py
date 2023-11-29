#daniel brito
"""
funçao que devolve True or False se o ano é bissexto ou não
"""

def anobissexto(ano):
    if (ano%400==0) or (ano%4==0 and ano%100!=0):
        return True
    else:
       return False
    
def main():
    ano=int(input('Diga o ano:'))
    print(anobissexto(ano))


if __name__ == "__main__":
    main()
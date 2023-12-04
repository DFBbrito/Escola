#Daniel Brito
"""
funçao que le um numero e diz true se for primo e false se nao é primo
!primo quando é divisor por ele ou por um!
"""
def primo(x):
    for i in range(2,x):
        resto=x%i
        if resto==0:
            print('Nao é primo')
            return
    print("É primo")

def main():
    x=int(input('Um nº: '))
    primo(x)

if __name__ == "__main__":
    main()
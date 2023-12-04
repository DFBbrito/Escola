#Daniel Brito
"""
Uma funçao que calcula a tabuada de um numero que lhe é passado
"""
def tabuada(x):
    for i in range(1,11):
        r=x*i
        print(f'{i}x{x}={r}')

def main():
    x=int(input('Um nº para fazer a tabuada: '))
    tabuada(x)

if __name__ == "__main__":
    main()

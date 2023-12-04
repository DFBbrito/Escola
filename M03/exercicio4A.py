#
"""
funçao que calcula a tabuada em uma variravel global
"""
x=int(input('um nº: '))

def tabuada():
    global x
    for i in range(1,11):
        r=x*i
        print(f'{i}x{x}={r}')
    x=0

def main():
    tabuada()

if __name__ == "__main__":
    main()


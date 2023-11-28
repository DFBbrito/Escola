#daniel brito
"""
"""
nome = "joaquim"
resultado=0
x=0
y=0

def cumprimentarV3():
    print(f'Bom dia {nome}!')

def somar():
    global x,y,resultado
    resultado=x+y
    x=0

def main():
    global x,y
    x=10
    y=5
    somar()
    print(resultado)


if __name__ == "__main__":
    main()
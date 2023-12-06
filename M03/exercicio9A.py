"""
Crie uma funçao que conta o numero de vogais em uma string
"""
import sys
def vogais(palavra):
    contar=0
    for letra in palavra:
        if letra in "AEIOUaeiou":
            contar+=1
    print(contar)


def main():
    if len(sys.argv) != 2:
        palavra=input("Insira uma palavra:")
    else:
        palavra=sys.argv[1]
    vogais(palavra)

if __name__ == "__main__":
    main()

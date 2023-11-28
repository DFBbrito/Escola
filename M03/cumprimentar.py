#Daniel Brito#
"""
Funçao: cumprimentar as pessoas e dizer bom dia
"""
def cumprimentar():
    print("Bom dia!")

def cumprimentarV2():
    nome=input('Diga o seu nome: ')
    print(f'Bom dia {nome}!')


def cumprimentarV3(nome):
    print(f'Bom dia {nome}!')
    nome=''



def main():
    nome=input('Diga o seu nome: ')
    cumprimentarV3(nome)
    print(nome)


if __name__ == '__main__':
    main()



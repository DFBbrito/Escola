"""
Alterar a função anterior para receber um nome e imprimir “Olá, nome”
"""
def saudar(nome):
    print(f'Olá, {nome}!')

def main():
    nome=input('Diga o seu nome: ')
    saudar(nome)

if __name__ == "__main__":
    main()
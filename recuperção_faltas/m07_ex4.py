"""
4. Manipulação Básica de Ficheiros de Texto
Objetivo: Criar um programa que leia um ficheiro de texto e imprima o seu conteúdo na tela, linha 
por linha.
Instruções:
1. Crie um ficheiro de texto chamado `exemplo.txt` e escreva algumas linhas de texto nele.
2. Abra o ficheiro para leitura usando a sintaxe `with`.
3. Leia o ficheiro linha por linha e imprima cada linha na tela
"""
# Criação do ficheiro exemplo.txt com algumas linhas de texto
with open('exemplo.txt', 'w') as ficheiro:
    ficheiro.write("primeira linha do ficheiro.\n")
    ficheiro.write("segunda linha do ficheiro.\n")
    ficheiro.write("terceira linha do ficheiro.\n")

def ler_ficheiro(nome_ficheiro):
    try:
        with open(nome_ficheiro, 'r') as ficheiro:
            for linha in ficheiro:
                print(linha, end='')  
    except FileNotFoundError:
        print(f"O ficheiro {nome_ficheiro} não foi encontrado.")

def main():
    nome_ficheiro = "exemplo.txt"
    ler_ficheiro(nome_ficheiro)

if __name__ == "__main__":
    main()


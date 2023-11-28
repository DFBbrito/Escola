#Daniel Brito#
"""
Xadrez 0.5V
Descrição
o tabuleiro de xadrez é um quadrado 8x8.
Cada casa do tabuleiro deve ser representada por um asterisco (*) para casas pretas e um espaço para casas brancas.
cada linha do tabuleiro deve começar com uma casa branca e alternar entre espaço e asterisco.
a linha seguinte deve começar com uma casa preta e alternar entre asterisco e espaço.
"""
for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            print('*', end="")
        else:
            print('_',end="")
    print("\n")


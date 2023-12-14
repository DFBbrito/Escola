#Daniel Brito
"""
Jogo do galo
"""
def DesenhaTabuleiro(tabuleiro):
    for letra in tabuleiro:
        if letra=="|":
            print("")
        else:
            print(letra,end="")
    print("")

def LerJogada(jogador,tabuleiro):
    linha=int(input('Linha:'))
    coluna=int(input('Coluna:'))
    posicao=
    return tabuleiro

def Vitoria(tabuleiro):
    pass

def main():
    jogador="x"
    tabuleiro="---|---|---"
    DesenhaTabuleiro(tabuleiro)
    while True:
        tabuleiro=LerJogada(jogador,tabuleiro)
        DesenhaTabuleiro(tabuleiro)
        if Vitoria(tabuleiro):
            break
        if jogador=="x":
            jogador="o"
        else:
            jogador="x"

if __name__ == "__main__":
    main()
"""
#tudo começa aqui
n_jogos

local
golos

max_golos
jornada_m_g
perc_j_casa
total
se fizeste isto
#agora melhora o codigo
"""
import numpy as np

def LerDados(n_jogos,locais,golos):
    #ler dados
    for i in range(n_jogos):
        #ler o local do jogo
        locais[i]=input(f"Qual o local do jogo nº {i+1}:")
        golos[i]=int(input(f"Quantos golos foram marcados no nª {i+1}:"))

def MaxGolos(n_jogos,golos):
    #maximo de golos e a jornada
    max_golos=golos[0]
    jornada_m_g=0
    for i in range(n_jogos):
        if golos[i]>=max_golos:
            max_golos=golos[i]
            joranada_m_g=i
    return f"O recorde de golos num jogo foi de {max_golos}, obtido na {joranada_m_g+1}ª jornada."

def CalcularJogosCasa(n_jogos,locais):
    #percentagem de jogos em casa(Viseu)
    contar_jogos_casa=0
    for i in range(n_jogos):
        if locais[i].lower()=="viseu":
            contar_jogos_casa+=1

    percentagens_jogos_casa=contar_jogos_casa/n_jogos*100
    return percentagens_jogos_casa

def CalcularTotalGolos(n_jogos,golos):
    #total de golos
    total=0
    for i in range(n_jogos):
        total=total+golos[i]
    return total

def main():
    #quantos jogos?
    n_jogos=int(input("Quantos jogos?"))
    while n_jogos<=0:
        print("o nº de jogos tem de ser superior a 0.")
        n_jogos=int(input("Quantos jogos?"))

    #definir um array para os locais
    locais=np.empty(n_jogos,'U20')
    golos=np.empty(n_jogos,'i')

    LerDados(n_jogos,locais,golos)

    mensagem=MaxGolos(n_jogos,golos)
    percentagens_jogos_casa=CalcularJogosCasa(n_jogos,locais)
    total=CalcularTotalGolos(n_jogos,golos)
    mensagem+=f" {percentagens_jogos_casa:.0f}% dos jogos da temporada em casa. A equipa marcou {total} golos na totalidade."
    print(mensagem)




if __name__ == "__main__":
    main()
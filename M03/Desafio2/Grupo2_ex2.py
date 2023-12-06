"""
Correção
2. escreva uma funçao que recbe três valores e devolve o maior, caso sejam todos positivos,caso os 
valores sejam todos negativos deve devolver o menor. Nas restantes situaçoes devolve None.
"""
def MaiorOuMenor(x1,x2,x3):
    #maior
    if x1>=x2 and x1>=x3:
        maior=x1
    elif x2>=x3:
        maior=x2
    else:
        maior=x3
    #menor
    if x1<=x2 and x1<=x3:
        menor=x1
    elif x2<=x3:
        menor=x2
    else:
        menor=x3
    #positivos
    if x1>0 and x2>0 and x3>0:
        return maior
    #negativos
    elif x1<0 and x2<0 and x3<0:
        return menor
    else:
        return None

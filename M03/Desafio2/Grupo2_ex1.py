"""
Correção
1.desenvolva uma funçao que recebe uma string e devolve verdadeiro e devolve verdadeiro se todas as letras da 
string sao iguais e falso nos restantes casos:
"""
def LetrasIguais(texto):
    for letra in texto:
        if letra!=texto[0]:
            return False
    return True


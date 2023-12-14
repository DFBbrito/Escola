#Daniel Brito
"""10. Uma função que recebe uma string com um valor binário e devolve um valor em base 10.
"""
def converterbase10(valorbinario):
    soma=0
    expoente=len(valorbinario)-1
    for posicao in range(len(valorbinario)):
        if valorbinario[posicao]=='1':
            soma = soma + 2**expoente
        expoente=expoente-1
    return soma


base10=converterbase10('1011')
print(base10)

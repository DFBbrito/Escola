"""
Correção
2. Crie uma funçao que mostre a media de 5 valores. A funçao deve ler os valores do utilizador e,
posteriormente,calcular e mostrar a média dos valores.
"""
def Media():
    soma=0
    for i in range(5):
        n=int(input('Valor: '))
        #Somar o valor
        soma+=n
    media=soma/5
    print(media)

Media()
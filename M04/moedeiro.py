#Daniel Brito
"""
Programa para gerir um moedeiro de uma maquina de vending
O programa deve permitir inserir os stock de moedas existente
Depois de perguntar o valor a pagar e o dinheiro entregue o programa 
deve calcular o troco e as moedas que perfazem o valor do troco.
Podem nao ser possivel devolver o troco por falta de meodas
"""
import numpy as np

moedeiro=np.array([[0.01,0],[0.02,0],[0.05,0],[0.1,0],[0.2,0],[0.5,0],[1,0],[2,0]])

#perguntar ao utilizador quantas moedas de cada tipo exitem no moedeiro
for l in range(moedeiro.shape[0]):
    stock_moeda=int(input(f"Quantas moedas de {moedeiro[l,0]}€ tem: "))
    moedeiro[l,0]=stock_moeda

#quanto dinheiro paga 
valor_a_pagar=float(input('Qual o valor a pagar: '))
#quanto dinheiro da 
dinheiro_entregue=float(input('Insira o dinheiro: '))
#dar troco
troco=dinheiro_entregue-valor_a_pagar
if troco>0:
    trocoAMT=troco
    print(f'Vai receber {troco:.2f}€')
#moedas a retirar moedeiro
    while troco>0:
        for t in range(moedeiro.shape[0],-1,-1):
            if moedeiro[t,0]<=troco and moedeiro[t,1]>0:
                moedeiro[t,1]-=1
                print(f"recebe uma moeda de {moedeiro[t,0]}")
                troco-=moedeiro[t,0]
                break
        if trocoAMT==troco:
            print("Nao tenho moedas para devolver o troco. Fico a dever {troco} ")
            break


#Daniel Brito
"""
Programa para gerir um moedeiro de uma maquina de vending
O programa deve permitir inserir os stock de moedas existente
Depois de perguntar o valor a pagar e o dinheiro entregue o programa 
deve calcular o troco e as moedas que perfazem o valor do troco.
Podem nao ser possivel devolver o troco por falta de meodas
"""
import numpy as np

moedeiro=np.array([[0.05,0],[0.1,0],[0.2,0],[0.5,0],[1,0],[2,0]])

#perguntar ao utilizador quantas moedas de cada tipo exitem no moedeiro

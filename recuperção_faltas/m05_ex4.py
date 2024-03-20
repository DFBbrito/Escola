"""
4-Escreva uma funçao que receba uma lista de ddicionarios(cada dicionario representando um produto com seu preço e quantidade) e retorne o valor total do estoque
"""
def total_estoque(produtos):
    total = 0
    for produto in produtos:
        preco=produto.get('preco',0)
        quantidade=produto.get('quantidade',0)
        if preco>0 and quantidade>0:
            total+=preco*quantidade
    return total

produtos=[
    {'nome': 'Produto 1', 'preco': 10, 'quantidade': 5},
    {'nome': 'Produto 2', 'preco': 20, 'quantidade': 3},
    {'nome': 'Produto 3', 'preco': 30, 'quantidade': 1},
]

total=total_estoque(produtos)
print(f'O valor total do estoque é: {total}')
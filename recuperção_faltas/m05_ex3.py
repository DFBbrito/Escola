"""
3-Crie um dicionario de stock de uma loja, opnde as chaves sao nomes de produtos e os valores sao as quantidades em stock. Em seguida, escreva uma funçao que recebe esse dicionario e um produto comno entrada e retorna a quantidade desse produto em stock
"""
inventario={'produto1':10,'produto2':5,'produto3':20}

def obter_estoque(inventario,produto):
    return inventario.get(produto,0)

estoque_produto1=obter_estoque(inventario,'produto1')
estoque_produto2=obter_estoque(inventario,'produto2')
estoque_produto3=obter_estoque(inventario,'produto3')

print(f"Estoque do produto1:{estoque_produto1}")
print(f"Estoque do produto2:{estoque_produto2}")
print(f"Estoque do produto3:{estoque_produto3}")
"""
1-crie um dicionario com informaçoes de pelo menos tres pessoas, como nome, idade e cidade.
Em seguida, imprima cada informaçao para cada pessoa.
"""
pessoas={
    1:{"nome":"Matateu","idade":40,"cidade":"Lisboa"},
    2:{"nome":"Galileu","idade":79,"cidade":"Porto"},
    3:{"nome":"Daniel","idade":16,"cidade":"Viseu"}
}

for pessoa in pessoas.values():
    print(f"Nome:{pessoa['nome']}")
    print(f"Idade:{pessoa['idade']}")
    print(f"Cidade:{pessoa['cidade']}")
    print()

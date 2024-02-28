nomes_1={"joaquim","ana","maria"}
nomes_2=("António","carla","joaquim","maria")

#mostrar todos os nomes
#fazer uniao dos dois conjuntos
uniao=nomes_1.union(nomes_2)
print(uniao)

#mostrar os nomes que existem em nomes_1 e ñ existem em nomes_2
#diferença
nomes_so_em_1=nomes_1.difference(nomes_2)
print(nomes_so_em_1)

#mostrar os nomes comuns aos dois conjuntos
#intersecçao
comuns=nomes_1.intersection(nomes_2)
print(comuns)

#adicionar um nome novo ao primeiro set
nomes_1.add("pai natal")
print(nomes_1)

#verificar se um nome existe nums er
if "pai natal" in nomes_1:
    print("pai natal está no conjunto 1")
else:
    print("não existe o pai natal no conjunto 1")
import pickle

NOME_FICHEIRO="dados.dat"

with open(NOME_FICHEIRO,"rb") as ficheiro:
    while True:
        try:
            dicionario=pickle.load(ficheiro)
        except EOFError:
            break
print(dicionario)

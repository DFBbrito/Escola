import pickle

NOME_FICHEIRO="lista.dat"

with open (NOME_FICHEIRO,"rb") as ficheiro:
    while True:
        try:
            lista=pickle.load(ficheiro)
            print(lista)
        except EOFError:
            print("Ocorreu um erro")
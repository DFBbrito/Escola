import pickle

dicionario={"nome":"joaquim",
            "idade":33,
            "email":"joaquim@gmail"}

NOME_FICHEIRO="dados.dat"

with open(NOME_FICHEIRO,"ab") as ficheiro:
    pickle.dump(dicionario,ficheiro)


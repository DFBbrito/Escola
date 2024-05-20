import pickle


with open('minha_lista', 'wb') as ficheiro:
    pickle.dump(minha_lista, ficheiro)
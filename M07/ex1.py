"ler 10 nomes e gravar no ficheiro de texto"

with open("nomes.txt","w",encoding="utf-8") as ficheiro:
    for i in range(10):
        nomes=input("diga um nome:")
        ficheiro.write(nomes+"\n")
    print("Dados guardados com sucesso!") 
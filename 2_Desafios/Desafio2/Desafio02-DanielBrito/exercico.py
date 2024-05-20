import pickle,os

NOME_FICHEIRO="dados.dat"

def adicionar():
    matricula=(input("Matricula:"))
    marca=input("Marca:")  
    modelo=input("Modelo:")
    ano=input("Ano:")
    #guardar no ficheiro binario
    with open(NOME_FICHEIRO,"ab") as ficheiro:
        novo={
            "matricula":matricula,
            "marca":marca,
            "modelo":modelo,
            "ano":ano
        }
        pickle.dump(novo,ficheiro)
    print("Dados guardados com sucesso!")

def listar():
    if os.path.exists(NOME_FICHEIRO)==False:
        print("Ainda não tem veiculos")
        return
    with open(NOME_FICHEIRO,"rb") as ficheiro:
        while True:
            try:
                veiculo=pickle.load(ficheiro)
                print(veiculo)
            except EOFError:
                break

def pesquisar():
    if os.path.exists(NOME_FICHEIRO)==False:
        print("Ainda não tem veiculos")
        return
    marca=input("Qual a marca a pesquisar?")
    with open(NOME_FICHEIRO,"rb") as ficheiro:
        while True:
            try:
                veiculo=pickle.load(ficheiro)
                if marca==veiculo["marca"]:
                    print(veiculo)
            except EOFError:
                break

def remover():
    if os.path.exists(NOME_FICHEIRO)==False:
        print("Ainda não tem veiculos")
        return
    matricula=input("Qual a matricula a remover:")
    contar=0
    with open(NOME_FICHEIRO,"rb") as ficheiro:
        with open("temp.dat","wb") as ficheiro_escrita:
            while True:
                try:
                    veiculo=pickle.load(ficheiro)
                    if matricula==veiculo["matricula"]:
                        contar+=1
                    else:
                        pickle.dump(veiculo,ficheiro_escrita)
                except EOFError:
                    break
    print(f"Foram removidos {contar} veiculos")
    os.remove(NOME_FICHEIRO)
    os.rename("temp.dat",NOME_FICHEIRO)

def extra_mais_10_anos():
    if os.path.exists(NOME_FICHEIRO)==False:
        print("Ainda não tem veiculos")
        return
    with open(NOME_FICHEIRO,"rb") as ficheiro:
        while True:
            try:
                veiculo=pickle.load(ficheiro)
                if int(veiculo["ano"])>10:
                    print(veiculo)
            except EOFError:
                break

def extra_contar_marcas():
    if os.path.exists(NOME_FICHEIRO)==False:
        print("Ainda não tem veiculos")
        return
    marcas={}
    with open(NOME_FICHEIRO,"rb") as ficheiro:
        while True:
            try:
                veiculo=pickle.load(ficheiro)
                if veiculo["marca"] in marcas:
                    marcas[veiculo["marca"]]+=1
                else:
                    marcas[veiculo["marca"]]=1
            except EOFError:
                break
    marcar_mais=""
    maior=0
    for marca, contagem in marcas.items():
        if contagem>maior:
            maior=contagem
            marcar_mais=marca
    print(f"A marca com mais veiculos é {marcar_mais} com {maior} veiculos")


def main(): 
    while True:
        op=int(input("1.Adicionar\n2.Listar\n3.Pesquisar\n4.Remover\n5.Terminar"))
        if op==1:
            adicionar()
        elif op==2:
            listar()
        elif op==3:
            pesquisar()
        elif op==4:
            remover()
        elif op==5:
            break
        else:
            print("Opção inválida") 

if __name__=="__main__":
    main()
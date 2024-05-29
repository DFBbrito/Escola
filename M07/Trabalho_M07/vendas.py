#Daniel Brito
import os
from camioes import carregar_camioes,guardar_camioes

FICHEIRO_VENDAS = "vendas.dat"

def validar_matricula(matricula):  
    if len(matricula)==8 and matricula[2]=="-" and matricula[5]=="-":
        return matricula
    else:
        print("Por favor, insira uma matricula válida.")

def realizar_venda():
    #obter os dados
    print("\n--- Realizar Venda ---")
    matricula=input("Matricula do camião a vender: ").strip().upper()
    #validar a matricula
    if validar_matricula(matricula)==False:
        print("Por favor, insira uma matricula válida.")
        return
    #carregar os dados
    camioes=carregar_camioes()
    #procurar o camião
    camiao_encontrado=None
    for camiao in camioes:
        if camiao['matricula']==matricula:
            camiao_encontrado=camiao
            break
    #realizar a venda
    if camiao_encontrado!=None:
        if camiao_encontrado.get("vendido")==None:
            preco=camiao_encontrado.get("preco")
            op=input(f"Confirma a venda do camião {matricula} por {preco}€? (SIM/NAO): ").strip().upper()
            if op=="S" or op=="SIM" or op=="Y" or op=="YES":
                #remover o camião
                camioes.remove(camiao_encontrado)
                #salvar os dados
                guardar_camioes(camioes)
                #registrar a venda
                registrar_venda(matricula,preco)
                print("Venda realizada com sucesso!")
            else:
                print("Venda cancelada.")
        else:
            print("Este camião ja foi vendido anteriormente.")
    else:
        print("Camião não encontrado.")

def registrar_venda(matricula,preco):
    #registrar a venda
    with open(FICHEIRO_VENDAS, "a") as ficheiro:
        ficheiro.write(f"Matricula: {matricula}\n Preço: {preco}€\n")

def listar_vendas():
    #listar as vendas
    print("\n---Registro de Vendas---")
    #carregar os dados
    if os.path.exists(FICHEIRO_VENDAS):
        #ler o ficheiro
        with open(FICHEIRO_VENDAS, "r") as ficheiro:
            #ler o conteudo
            print("Vendas:")
            for linha in ficheiro:
                print(linha.strip())
    else:
        print("Ainda não existem vendas.")

def main():
    while True:
        print("\n---Menu de Vendas---")
        print("1. Realizar Venda")
        print("2. Listar Vendas")
        print("3. Voltar ao Menu Principal")
        op=input("Escolha uma opção: ").strip()
        if op=="1":
            realizar_venda()
        elif op=="2":
            listar_vendas()
        elif op=="3":
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()

#Daniel Brito
import pickle,os

NOME_FICHEIRO="camioes.dat"

def adicionar_camiao():
    #obter os dados
    print("\n---Adicionar Camião---")
    print("Insira os dados do camião:")
    matricula=obter_matricula()
    modelo=input("Modelo do camião: ").strip()
    ano=obter_ano()
    preco=obter_preco()
    #criar o dicionário
    novo_camiao = {
        "matricula":matricula,
        "modelo":modelo,
        "ano":ano,
        "preco":preco
    }
    #adicionar ao ficheiro
    camioes=carregar_camioes()
    for camiao in camioes:
        if camiao['matricula'] == matricula:
            return "Camião ja existe."
    camioes.append(novo_camiao)
    guardar_camioes(camioes)
    print("Camião adicionado com sucesso!")

def obter_matricula():  
    #obter os dados
    while True:
        matricula=input("Matricula do camião:").strip().upper()
        #validar a matricula
        if len(matricula)==8 and matricula[2]=="-" and matricula[5]=="-":
            return matricula
        else:
            print("Por favor, insira uma matricula válida.")

def obter_ano():
    #obter os dados
    while True:
        ano=input("Ano do camião:").strip().upper()
        #validar o ano
        if ano.isdigit() and len(ano) == 4 and int(ano) > 0:
            return ano
        else:
            print("Por favor, insira um ano válido (4 dígitos).")

def obter_preco():
    #obter os dados
    while True:
        preço=input(str("Preço do camião: "))
        #validar o preco 
        try:
            preço=float(preço)
            if preço>0 and isinstance(preço,float) or isinstance(preço,int):
                return preço
            else:
                print("O preço deve ser maior que zero.")
        except ValueError:
            print("Por favor, insira um preço válido.")

def carregar_camioes():
    #carregar os dados
    #verificar se o ficheiro existe
    if os.path.exists(NOME_FICHEIRO):
        with open(NOME_FICHEIRO, "rb") as ficheiro:
            return pickle.load(ficheiro)
    else:
        return []

def guardar_camioes(camioes):
    #salvar os dados
    with open(NOME_FICHEIRO, "wb") as ficheiro:
        pickle.dump(camioes,ficheiro)

def listar_camioes():
    print(f"Existem {len(carregar_camioes())} camiões.")
    #carregar os dados
    camioes=carregar_camioes()
    #listar os dados
    if camioes:
        print("\n---Lista de Camiões---")
        for camiao in camioes:
            print(f"Matricula: {camiao['matricula']},\nModelo: {camiao['modelo']},\nAno: {camiao['ano']},\nPreço: {camiao['preco']}€\n")
    else:
        print("Ainda não existem camiões.")

def remover_camiao():
    matricula=input("Matricula do camião a ser removido: ").strip().upper()
    #carregar os dados
    camioes=carregar_camioes()
    #remover os dados
    camioes=[camiao for camiao in camioes if camiao['matricula']!=matricula]
    #salvar os dados
    guardar_camioes(camioes)
    print("Camião removido com sucesso.")

def main():
    while True:
        print("\n--- Menu de Gerenciamento de Camiões ---")
        print("1. Adicionar Camião")
        print("2. Listar Camiões")
        print("3. Remover Camião")
        print("4. Voltar ao Menu Principal")
        op=input("Escolha uma opção: ")
        if op=="1":
            adicionar_camiao()
        elif op=="2":
            listar_camioes()
        elif op=="3":
            remover_camiao()
        elif op=="4":
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()

# compras.py

import os,pickle
from camioes import carregar_camioes, guardar_camioes

FICHEIRO_COMPRAS="compras.dat"

def realizar_compra():
    print("\n--- Realizar Compra ---")
    matricula=input("Matricula do camião: ").strip().upper()
    marca=input("Marca do camião: ").strip()
    modelo=input("Modelo do camião: ").strip()
    ano=input("Ano do camião: ").strip()
    preco=float(input("Preço do camião: "))
    # Verifica se o camião já foi adicionado anteriormente
    camioes=carregar_camioes()
    for camiao in camioes:
        if camiao["matricula"] == matricula:
            return "Este camião já foi adicionado anteriormente."
    # Adiciona o camião à lista de camiões
    novo_camiao = {"matricula":matricula, "marca":marca, "modelo":modelo, "ano":ano, "preco":preco}
    camioes.append(novo_camiao)
    guardar_camioes(camioes)
    #Adiciona o camiao ao stand
    adicionar_stand(matricula,marca,modelo,ano,preco)
    # Registra a compra
    registrar_compra(matricula,marca,modelo,ano,preco)
    print("Compra realizada com sucesso!")

def adicionar_stand(matricula,marca,modelo,ano,preco):
    with open("camioes.dat","a") as ficheiro:
        ficheiro.write(f"Matricula: {matricula}, Marca: {marca}, Modelo: {modelo}, Ano: {ano}, Preço: {preco}€\n")

def registrar_compra(matricula, marca, modelo, ano, preco):
    with open(FICHEIRO_COMPRAS, "a") as arquivo:
        arquivo.write(f"Matricula: {matricula}, Marca: {marca}, Modelo: {modelo}, Ano: {ano}, Preço: {preco}€\n")

def listar_compras():
    print("\n--- Lista de Compras ---")
    if os.path.exists(FICHEIRO_COMPRAS):
        with open(FICHEIRO_COMPRAS, "r") as arquivo:
            print(arquivo.read())
    else:
        print("Ainda não há compras registradas.")

def main():
    while True:
        print("\n--- Menu de Compras ---")
        print("1. Realizar Compra")
        print("2. Listar Compras")
        print("3. Voltar ao Menu Principal")
        op=input("Escolha uma opção: ").strip()
        if op == "1":
            realizar_compra()
        elif op == "2":
            listar_compras()
        elif op == "3":
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()

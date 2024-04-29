#Daniel Brito
import camioes_stand

compras=[]

def comprar_camiao(matricula,modelo,preço):
    compra={"matricula":matricula,"modelo":modelo,"preço":preço}
    compras.append(compra)
    camioes_stand.adicionar_camiao(matricula,modelo,preço)
    return (f"Camiao {matricula} comprado e adicionado ao stand")

def listar_compras():
    visualizaçao=[]
    for compra in compras:
        detalhes=(f"Camiao {compra['modelo']} e matricula {compra['matricula']} comprado.")
        visualizaçao.append(detalhes)
    return visualizaçao

def menu_compras():
    while True:
        print("\n--- Menu de Compras ---")
        print("1. Comprar Camião")
        print("2. Listar Compras")
        print("3. Voltar ao Menu Principal")
        op=input("Escolha uma opção: ")
        if op=="1":
            matricula=input("\nInsira a matricula do camião: ")
            modelo=input("Insira o modelo do camião: ")
            preco=float(input("Insira o preço do camião: "))
            print(comprar_camiao(matricula,modelo,preco))
        elif op=="2":
            print("\nCamioes comprados:")
            for detalhes in listar_compras():
                print("-"*15)
                print(detalhes)
        elif op=="3":
            break
        else:
            print("Opção inválida, tente novamente.")
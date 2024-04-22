import camioes_stand

vendas=[]

def vender_camiao(matricula,cliente_nome):
    for camiao in camioes_stand.camioes_stand:
        if camiao["matricula"]==matricula:
            venda={"matricula":matricula,"cliente":cliente_nome,"preço":camiao["preço"]}
            vendas.append(venda)
            camioes_stand.remover_camiao(matricula)
            return (f"Camiao {matricula} vendido ao {cliente_nome}")
    return ("Camiao nao encontrado no stand")

def listar_vendas():
    return vendas

def menu_vendas():
    while True:
        print("--- Menu de Vendas ---")
        print("1. Vender Camião")
        print("2. Listar Vendas")
        print("3. Voltar ao Menu Principal")
        op=input("Escolha uma opção: ")
        if op=="1":
            matricula=input("Insira a placa do camião: ")
            cliente_nome=input("Insira o nome do cliente que quer comprar o camião: ")
            print(vender_camiao(matricula,cliente_nome))
        elif op=="2":
            print("Vendas feitas:",listar_vendas())
        elif op=="3":
            break
        else:
            print("Opção inválida, tente novamente.")
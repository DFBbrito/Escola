#Daniel Brito
camioes_stand=[
    {"matricula":"AA-12-43","modelo":"Volvo FH","preço":75000},
    {"matricula":"10-BB-45","modelo":"Scania R450","preço":85000},
    {"matricula":"16-06-CC","modelo":"Mereceds Actro","preço":95000},
]

def validar_placa(matricula):
    if len(matricula)>0 and len(matricula)<=8:
        return True
    return False

def adicionar_camiao(matricula,modelo,preço):
    camiao={"matricula":matricula,"modelo":modelo,"preço":preço}
    camioes_stand.append(camiao)
    return (f"Camiao {matricula} adicionado ao stand")

def remover_camiao(matricula):
    for camiao in camioes_stand:
        if camiao["matricula"]==matricula:
            camioes_stand.remove(camiao)
            return (f"Camião {matricula} removido do stand.")
    return ("Camião não encontrado no stand.")

def listar_camioes():
    for camiao in camioes_stand:
        detalhes=(f"\nMatricula: {camiao['matricula']}\nModelo: {camiao['modelo']}\nPreço: {camiao['preço']}")
    return detalhes,camioes_stand

def menu_camioes():
    while True:
        print("--- Menu de Camiões ---")
        print("1. Adicionar Camião")
        print("2. Remover Camião")
        print("3. Listar Camiões")
        print("4. Voltar ao Menu Principal")
        op=input("Escolha uma opção: ")
        if op=="1":
            matricula=input("Insira a matricula do camião: ")
            modelo=input("Insira o modelo do camião: ")
            preco=float(input("Insira o preço do camião: "))
            print(adicionar_camiao(matricula,modelo,preco))
        elif op=="2":
            matricula=input("Insira a matricula do camião a remover: ")
            print(remover_camiao(matricula))
        elif op=="3":
            print("Camiões no stand:", listar_camioes())
        elif op=="4":
            break
        else:
            print("Opção inválida, tente novamente.")

#Daniel Brito
clientes=[]

def adicionar_cliente(nome,contacto):
    cliente={"nome":nome,"contacto":contacto}
    clientes.append(cliente)
    return (f"Cliente {nome} adicionado.")

def remover_cliente(nome):
    for cliente in clientes:
        if cliente["nome"]==nome:
            clientes.remove(cliente)
            return (f"Cliente {nome} removido.")
    return ("Cliente não encontrado.")

def editar_cliente(nome):
    novo_nome=None
    novo_contacto=None
    for cliente in clientes:
        if cliente["nome"]==nome:
            if novo_nome:
                cliente["nome"]=novo_nome
            if novo_contacto:
                cliente["contacto"]=novo_contacto
            return (f"Cliente {nome} atualizado.")
    return ("Cliente não encontrado.")

def listar_clientes():
    visualizaçao=[]
    for cliente in clientes:
        detalhes=(f"Nome: {cliente['nome']}\nContacto: {cliente['contacto']}")
        visualizaçao.append(detalhes)
    return visualizaçao

def menu_clientes():
    while True:
        print("\n--- Menu de Clientes ---")
        print("1. Adicionar Cliente")
        print("2. Remover Cliente")
        print("3. Editar Cliente")
        print("4. Listar Clientes")
        print("5. Voltar ao Menu Principal")
        op=input("Escolha uma opção: ")
        if op=="1":
            nome=input("\nInsira o nome do cliente: ")
            contacto=input("Insira o contacto do cliente: ")
            print(adicionar_cliente(nome,contacto))
        elif op=="2":
            nome=input("\nInsira o nome do cliente a remover: ")
            print(remover_cliente(nome))
        elif op=="3":
            nome=input("\nInsira o nome do cliente a editar: ")
            novo_nome=input("Novo nome (deixe vazio para não alterar): ")
            novo_contacto=input("Novo contacto (deixe vazio para não alterar): ")
            print(editar_cliente(nome,novo_nome,novo_contacto))
        elif op=="4":
            print("\nClientes:")
            for detalhes in listar_clientes():
                print("-"*15)
                print(detalhes)
        elif op=="5":
            break
        else:
            print("Opção inválida, tente novamente.")
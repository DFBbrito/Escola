#Daniel Brito
"""
Trabalho m06 
----------------
um programa para ajudar a gerir um stand de camioes de uma empresa
Requisitos:
    - Gestao de camioes a vender no stand
    - Gestao de clientes
    - Gestao de compras de camioes
    - Gestao de vendas de camioes
"""
import camioes_stand,clientes,compras,vendas

def main():
    while True:
        print("\n-----Menu Principal-----")
        print("1. Gerir Camiões no Stand")
        print("2. Gerir Clientes")
        print("3. Gerir Compras")
        print("4. Gerir Vendas")
        print("5. Sair")
        op=input("Escolha uma opçao:")
        if op=="1":
            camioes_stand.menu_camioes()
        elif op=="2":
            clientes.menu_clientes()
        elif op=="3":
            compras.menu_compras()
        elif op=="4":
            vendas.menu_vendas()
        elif op=="5":
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()

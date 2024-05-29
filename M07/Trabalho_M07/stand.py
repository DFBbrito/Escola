#Daniel Brito
import camioes,compras,vendas

def main():
    while True:
        print("\n---Menu Principal---")
        print("1. Gerir Camiões")
        print("2. Comprar Camião")
        print("3. Vender Camião")
        print("4. Sair")
        op=input("Escolha uma opção: ")
        if op=="1":
            camioes.main()
        elif op=="2":
            compras.main()
        elif op=="3":
            vendas.main()
        elif op=="4":
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()

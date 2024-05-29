"""
2.Crie um programa que lê o ficheiro de texto criado na questão anterior.
"""
def ler_nomes_do_ficheiro(nome_ficheiro):
    nomes=[]
    try:
        with open(nome_ficheiro,'r') as ficheiro:
            nomes=ficheiro.readlines()
        nomes=[nome.strip() for nome in nomes]
    except FileNotFoundError:
        print(f"O ficheiro {nome_ficheiro} não foi encontrado.")
    return nomes

def main():
    nome_ficheiro = "nomes.txt"
    nomes = ler_nomes_do_ficheiro(nome_ficheiro)
    if nomes:
        print("Nomes do ficheiro:")
        for nome in nomes:
            print(nome)

if __name__ == "__main__":
    main()

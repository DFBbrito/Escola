"""
3.Crie um programa que remove do ficheiro de texto os nomes repetidos.
"""
def ler_nomes_do_ficheiro(nome_ficheiro):
    nomes=[]
    try:
        with open(nome_ficheiro,'r') as ficheiro:
            nomes = ficheiro.readlines()
        nomes = [nome.strip() for nome in nomes] 
    except FileNotFoundError:
        print(f"O ficheiro {nome_ficheiro} não foi encontrado.")
    return nomes

def remover_duplicados(nomes):
    nomes_unicos=list(dict.fromkeys(nomes))  
    return nomes_unicos

def guardar_nomes_em_ficheiro(nomes, nome_ficheiro):
    with open(nome_ficheiro,'w') as ficheiro:
        for nome in nomes:
            ficheiro.write(nome+'\n')
    print(f"Os nomes únicos foram guardados em {nome_ficheiro} com sucesso.")

def main():
    nome_ficheiro="nomes.txt"
    nomes=ler_nomes_do_ficheiro(nome_ficheiro)
    if nomes:
        nomes_unicos=remover_duplicados(nomes)
        guardar_nomes_em_ficheiro(nomes_unicos,nome_ficheiro)
        print("Nomes duplicados foram removidos.")
        print("Nomes únicos:")
        for nome in nomes_unicos:
            print(nome)

if __name__ == "__main__":
    main()

"""
1.Crie um programa que lê o nome de 10 pessoas e guarda num ficheiro de texto.
"""
def ler_nomes():
    nomes=[]
    for i in range(10):
        nome=input(f"Nome da pessoa {i+1}: ").strip()
        nomes.append(nome)
    return nomes

def guardar_nomes(nomes,nome_ficheiro):
    with open(nome_ficheiro,'w') as ficheiro:
        for nome in nomes:
            ficheiro.write(nome+'\n')
    print(f"Os nomes foram guardados em {nome_ficheiro} com sucesso.")

def main():
    nome_ficheiro="nomes.txt"
    nomes=ler_nomes()
    guardar_nomes(nomes, nome_ficheiro)

if __name__ == "__main__":
    main()

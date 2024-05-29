"""
5. Escrevendo em um Ficheiro
Objetivo: Escrever dados em um ficheiro de texto, adicionando novas linhas a cada execução do 
programa.
Instruções:
1. Leia uma string do utilizador.
2. Abra um ficheiro com nome `dados.txt` em modo de anexação (`'a'`).
3. Escreva a string inserida pelo utilizador no ficheiro, seguida por uma quebra de linha.
4. Feche o ficheiro."""
def adicionar_dados():
    # Ler a string do utilizador
    dados = input("Digite o texto que deseja adicionar ao ficheiro: ").strip()

    # Abrir o ficheiro 'dados.txt' em modo de anexação
    with open('dados.txt', 'a') as ficheiro:
        # Escrever a string no ficheiro, seguida por uma quebra de linha
        ficheiro.write(dados + '\n')

    print("Dados adicionados ao ficheiro com sucesso.")

def main():
    adicionar_dados()

if __name__ == "__main__":
    main()

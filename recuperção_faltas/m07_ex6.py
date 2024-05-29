"""
6. Trabalhando com Ficheiros Binários
Objetivo: Copiar uma imagem usando manipulação de ficheiros binários.
Instruções:
1. Selecione uma imagem pequena para usar neste exercício.
2. Abra o ficheiro da imagem original em modo de leitura binária.
3. Leia todo o conteúdo do ficheiro.
4. Abra um novo ficheiro em modo de escrita binária e escreva o conteúdo lido.
5. Feche ambos os ficheiros."""
def copiar_ficheiro_binario():
    # Nome do ficheiro original e do ficheiro de destino
    ficheiro_origem = 'ficheiro_original.bin'
    ficheiro_destino = 'ficheiro_copia.bin'

    try:
        # Abrir o ficheiro original em modo de leitura binária
        with open(ficheiro_origem, 'rb') as f_origem:
            # Ler todo o conteúdo do ficheiro original
            conteudo = f_origem.read()
        
        # Abrir um novo ficheiro em modo de escrita binária
        with open(ficheiro_destino, 'wb') as f_destino:
            # Escrever o conteúdo lido no novo ficheiro
            f_destino.write(conteudo)
        
        print("Ficheiro binário copiado com sucesso.")
    
    except FileNotFoundError:
        print("O ficheiro original não foi encontrado.")

def main():
    copiar_ficheiro_binario()

if __name__ == "__main__":
    main()

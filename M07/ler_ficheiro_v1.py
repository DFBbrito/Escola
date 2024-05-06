"""programa para ler um ficheiro de texto"""
#abrir o ficheiro
ficheiro=open('meu_ficheiro.txt','r')
#ler o conteudo
texto=ficheiro.read()
#fechar o ficheiro
ficheiro.close()
#mostrar
print(texto)
 
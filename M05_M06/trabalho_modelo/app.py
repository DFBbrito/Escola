"""
Trabalho Modelo - Modulo 6
---------------------------
Um programa para ajudar a gerir os livros e emprestimos de uma biblioteca 
Requisitos:
    - Gestao Livros (CRUD)
    - Gestao leitores (CRUD)
    - Emprestimos/devoluçoes
    - Estatisticas (Top livro, top mês, top leitores)
"""
import utils

#em modo debug vamos fornecer leitores e livros de exemplo
DEBUG=True

def menu_principal():
    while True:
        utils.mostrar_menu("Menu Principal",["Livros","Leitores","Emprestimos e Devoluçoes","Estatisticas","Sair"])
        op=utils.le_numero("Opçao:")
        if op==5:
            break
        if op==1:
            pass
        if op==2:
            pass
        if op==3:
            pass
        if op==4:
            pass

def main():
    if DEBUG:
        pass
    menu_principal()

if __name__=="__main__":
    main()
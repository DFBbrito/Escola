"""
Programa para guardar dados de uma lista com vários alunos em um ficheiro de texto
Neste projeto os dados estão todos na lista durante a execução do programa
"""
import utils

#Lista dos alunos
alunos = []

#nome do ficheiro
nome_ficheiro = "alunos.txt"

def criar_aluno():
    """Função para ler os seguintes dados:
    Nome, morada, email e idade de um aluno
    Devolve um dicionário com os dados"""
    nome=utils.le_texto("Nome do aluno:")
    morada=utils.le_texto("Morada do aluno:")
    email=utils.le_email("Email do aluno:")
    idade=utils.le_numero("Idade do aluno:")
    novo_aluno={
        "nome":nome,
        "morada":morada,
        "email":email,
        "idade":idade
    }

def listar():
    """Função para listar os alunos da lista"""
    for aluno in alunos:
        print(aluno)


def adicionar():
    """Função para adicionar um aluno à lista"""
    novo_aluno=criar_aluno()
    alunos.append(novo_aluno)
    print (f"O aluno {novo_aluno['nome']} adicionado com sucesso\nTem {len(alunos)} alunos ")

def guardar():
    """Função para guardar todos os alunos num ficheiro de texto.
    Cada aluno deve ficar numa só linha com os seus dados separados por ,
    A primeira linha do ficheiro deve indicar quantos alunos existem no ficheiro"""
    with(open(nome_ficheiro,"w",encoding="utf-8")) as ficheiro:
        ficheiro.write(f"{len(alunos)}\n")
        for aluno in alunos:
            ficheiro.write(f"{aluno['nome']},{aluno['morada']},{aluno['email']},{aluno['idade']}\n")

def ler():
    """Função para ler os alunos do ficheiro para a lista"""
    pass

def main():
    while True:
        op=utils.menu("Ficheiros Texto",["Adicionar","Listar","Terminar"])
        if op==1:
            adicionar()
        if op==2:
            listar()
        if op==3:
            break

if __name__=="__main__":
    main()
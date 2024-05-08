"""
Programa para guardar dados de vários alunos em um ficheiro de texto
Neste projeto os dados estão todos só no ficheiro e são lidos/escritos quando é necessário
"""
import utils,os


#nome do ficheiro
nome_ficheiro = "alunos2.txt"

def criar_aluno():
    """Função para ler os seguintes dados:
    Nome, morada, email e idade de um aluno
    Devolve um dicionário com os dados"""
    nome=utils.le_texto("Nome do aluno:")
    morada=utils.le_texto("Morada do aluno:")
    email=utils.le_email("Email do aluno:")
    idade=utils.le_numero("Idade do aluno:")
    novo_aluno={"nome":nome,
                "morada":morada,
                "email":email,
                "idade":idade}
    return novo_aluno

def listar():
    """Função para listar os alunos do ficheiro"""
    if ficheiro_existe()==False:
        return
    #abrir o ficheiro para leitura
    with open(nome_ficheiro,"r",encoding="utf-8") as ficheiro:
        while True:
            linha_aluno=ficheiro.readline()
            if not linha_aluno:
                break
            linha_alunos=linha_aluno.split(",")
            print(linha_alunos)

def ficheiro_existe():
    if os.path.exists(nome_ficheiro)==False:
        print("Ficheiro não existe")
        return False
    return True

def adicionar():
    """Função para adicionar um aluno ao ficheiro"""
    aluno=criar_aluno()
    with open(nome_ficheiro,"a",encoding="utf-8") as ficheiro:
        ficheiro.write(f"{aluno['nome']},{aluno['morada']},{aluno['email']},{aluno['idade']}\n")
        print(f"Aluno {aluno['nome']} adicionado com sucesso")

def apagar():
    """Função para apagar um aluno do ficheiro"""
    if ficheiro_existe()==False:
        return
    nome=utils.le_texto("Nome do aluno a remover:")
    with open(nome_ficheiro,"r",encoding="utf-8") as f_leitura:
        with open("temp.txt","w",encoding="utf-8") as f_escrita:
            while True:
                linha_aluno=f_leitura.readline()
                if not linha_aluno:
                    break
                aluno=linha_aluno.split(",")
                apaguei=False
                if aluno[0]!=nome or apaguei==True:
                    f_escrita.write(linha_aluno)
                else:
                    apaguei=True
    #apagar ficheiro 
    os.remove(nome_ficheiro)
    #renomear o ficheiro temporaio
    os.rename("temp.txt",nome_ficheiro)

def pesquisar():
    nome=utils.le_texto("Nome do aluno:")
    with open(nome_ficheiro,"r",encoding="utf-8") as ficheiro:
        for linha_aluno in ficheiro:
            if nome in linha_aluno:
                print(linha_aluno)
                
def main():
    while True:
        op=utils.menu("Ficheiros Texto",["Adicionar","Listar","Apagar","Pesquisar","Terminar"])
        if op==1:
            adicionar()
        if op==2:
            listar()
        if op==3:
            apagar()
        if op==4:
            pesquisar()
        if op==5:
            break
if __name__=="__main__":
    main()
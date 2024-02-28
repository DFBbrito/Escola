
# Função que permite ao utilizador adicionar um livro
# O livro novo estará sempre disponivel
# Tenha atenção para não repetir o id do livro
def adicionar_livro(livros):
    titulo=input("Insira um titulo:")
    if len(livros)>0:
        bi=livros[len(livros)-1]["id_livro"]+1
    else:
        bi=1
    novo={'id_livro':bi,'titulo':titulo,'Disponivel':True,'nome_leitor':''}
    livros.append(novo)
     
# Função para mostrar os livros
# deve permitir escolher se lista todos ou só os disponíveis ou só os indisponíveis
def listar_livros(livros):
    print("1.listar todos\n2.listar disponiveis\n3.listar indisponivel")
    op=input(":")
    for livro in livros:
        if op=="1" or (op=="2"and livro["diponivel"]==True) or (op=="3" and livro["diponivel"]==False):
            for chave,valor in livro.items():
                print(f"{chave}:{valor}")
            print("-"*20)
# Função que muda o estado do livro e regista o nome do leitor
def emprestar_livro(livros):
    pass

#Função que torna o livro disponível e apaga o nome do leitor
def devolver_livro(livros):
    pass

#Função que apresenta as opções ao utilizador e devolve a sua escolha
def menu():
    while True:
        print("1. Adicionar\n2.Listar\n3.Emprestar\n4.Devolver\n5.Sair")
        op = int(input(":"))
        if op <1 or op >5:
            print("Essa opção não é válida")
        else:
            return op

#função para gerar (seed) dados iniciais
def inicializar(livros):
    livros.append({"id_livro":1,"titulo": "Dom Quixote", "disponivel": True,"nome_leitor":""})
    livros.append({"id_livro":2,"titulo": "A Arte da Guerra", "disponivel": True,"nome_leitor":""})
    livros.append({"id_livro":3,"titulo": "1984", "disponivel": True,"nome_leitor":""})
    livros.append({"id_livro":4,"titulo": "Os Lusíadas", "disponivel": True,"nome_leitor":""})
    livros.append({"id_livro":5,"titulo": "A Metamorfose", "disponivel": True,"nome_leitor":""})

def main():
    livros=[]
    inicializar(livros)
    while True:
        op=menu()
        if op==1:
            adicionar_livro(livros)
        elif op==2:
            listar_livros(livros)
        elif op==3:
            emprestar_livro(livros)
        elif op==4:
            devolver_livro(livros)
        elif op==5:
            break

# Ponto de entrada do programa (main loop)
if __name__ == "__main__":
    main()

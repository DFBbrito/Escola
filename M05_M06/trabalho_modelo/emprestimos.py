"""Módulo para gerir emprestimos/devoluçao"""
import leitores,livros, utils
import datetime

emprestimos=[]

def menu_emprestimos():
    while True:
        utils.mostrar_menu("Menu empréstimos",["Emprestar","Devolver","Livros emprestados","Leitores com livros","Voltar"])
        op=utils.le_numero("Opçao:")
        if op==5:
            break
        if op==1:
            emprestar()
        if op==2:
            devolver()
        if op==3:
            livros_emprestados()
        if op==4:
            leitores_com_livros()
        

def emprestar():
    """Funçao para registar o emprestimo de um livro"""
    #id do livro a emprestar
    id_livro=utils.le_numero("Id do livro a emprestar:")
    livro=livros.get_livro(id_livro)
    while livro is None:
        id_livro=utils.le_numero("O id indicado nao existe.\nId do livro a emprestar")
        livro=livros.get_livro(id_livro)
    #testar se o livro está disponivel
    if livro["estado"]!="disponivel":
        print("O livro não se encontra disponivel.")
        return
    #id do leitor
    id_leitor=utils.le_numero("Id do leitor:")
    leitor=leitores.get_leitor(id_leitor)
    if leitor is None:
        print("Esse leitor nao existe")
        return
    #Mostrar o livro e o leitor
    print(f"Emprestimos do livro {livro['Nome']} ao leitor {leitor['Nome']}")
    #guardar a data atual do computador 
    data_emprestimo=datetime.datetime.datetime.now()
    #calcular a data de entrega do livro (somar 7 dias à data atual)
    data_devoluçao=data_emprestimo+datetime.timedaelta(days=7)
    data_formatada=data_devoluçao.strftime("%d/%m/%Y")
    print(f"Tem de devolver o livro até {data_formatada}")
    #guardar na lista do emprestimos
    novo={
        "livro":livro,
        "leitor":leitor,
        "data_emprestimo":data_emprestimo,
        "data_devoluçao":data_devoluçao,
        "estado":'emprestado'
    }
    #alterar o estado do livro para emprestado
    livro["estado"]="emprestado"
    #guardar o leitor no livro emprestado
    livro["leitor"]=leitor
    livro["nr_emprestimos"]+=1
    emprestimos.append(novo)

def devolver():
    id_livro=utils.le_numero("Id do livro a devolver:")
    livro=livros.get_livro(id_livro)
    if livro is None:
        print("Esse livro não existe")
        return
    if livro['estado']!='emprestado':
        print("Esse livro não se encontra emprestado")
        return
    for emprestimo in emprestimos:
        if emprestimo["livro"]==livro and emprestimo["estado"]=="emprestado":
            if emprestimo["data_devoluçao"]>datetime.datetime.now():
                print("livro devolvido dentro do prazo.")
            else:
                print("Livro devolvido fora do prazo.")
            #alterar o estado do emprestimo
            emprestimo["estado"]="concluido"
            #alterar o estado do livro
            livro["estado"]="disponivel"
            #retirar o leitor do livro 
            livro["leitor"]=None
            return
    print("Os dados da aplicaçao estão corrompidos. CHAME A ASSISTÊNCIA.")

def livros_emprestados():
    for livro in livros.livros:
        if livro["estado"]=="emprestado":
            print(livro)

def leitores_com_livros():
    for livro in livros.livros:
        if livro["estado"]=="emprestado":
            print(livro["leitor"])


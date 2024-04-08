"""
Fazer a validaçao dos (), [] e {} de uma expressão
"""
import sys

#ler a expressao da linha de comando p.e:python validaçao.py '(10+5)/3"

argv=sys.argv
if len(argv)==1:
    expressao=input("Expressão e validar:")
else:
    expressao=argv[1]

#pares
pares={
    "(":")",
    "[":"]",
    "{":"}"
}
#para guardar os ( [ { a abrir
stack=[]

#flag para indicar estado da expressao
correto=True
#percorrer a expressao
for c in expressao:
    print(c)
    #cerificar se é um ( [ {
    if c in pares.keys():
        stack.append(c)
    elif c in pares.values():
        #verificar se tem um ( [ { 
        if len(stack)==0:
            print(f"Erro na expressão em {c}")
            correto=False
            break
        else:
            t=stack.pop()
            if pares[t]!=c:
                print(f"Erro na expressao em {c}")
                correto=False
                break

#Ficou algum ( [ { por fechar
if len(stack)!=0:
    print("Erro na expressão! Expressao incompleta.")
elif correto==True:
    print("Expressao correto")

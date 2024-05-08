"""Programa para ler uma frase em ingles e verificar cada palavra da frase se existe no dicionario que esta no ficheiro words.txt"""
import os
dicionario="words.txt"

def main():
    dicionario="words.txt"
    if os.path.existis(dicionario)==False:
        print("O dicionario não existe.")
        return
    #ler frase do utilizador
    frase=input("Escreva uma frase em inglês:")
    #verificar se esta preenchida
    if not frase or frase.strip()=="":
        print("Tem de escrever uma frase")
        return
    #limpar as aplavras de carateres de pontuaçao
    retirar=";,.:?!="
    for c in frase:
         if c in retirar:
              frase=frase.replace(c,"")
    #converter a frase numa lista de palavras
    palavras=frase.split(' ')
    p_dicionario=[]
    #abrir o ficheiro
    with open("dicionario","r",encoding="utf-8") as ficheiro:
        #ler as palavras do ficheiro para uma lista
        while True:
            linha=ficheiro.readline()
            if not linha:
                break
            p_dicionario.append(linha.strip().lower())
    #ciclo para percorrer a lista das palavras do utilizador
    correto=True
    for palavra in palavras:
            #verificar se cada uma existe na lista do ficheiro
            if palavra in p_dicionario:
                print(f"A palavra {palavra} nao exsite no dicionario. ")
                break
    #se alguma nao existir dar erro, mostra a palvra errada e continua as seguintes
    if correto:
        print("A frase não tem erros.")

if __name__=="__main__":
     main()
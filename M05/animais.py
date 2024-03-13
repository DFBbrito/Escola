animais={("cao","pitbull"):{"idade":5,"dono":"joaquim"},("tartaruga","ninja"):{"idade":10,"dono":"maria"}}
#->listar os animais (joao)´
for chave,valor in animais.items():
    if valor["dono"]=="joaquim":
        print(f"Especie: {chave[0]} \nRaça: {chave[1]} \nIdade: {valor['idade']}")

#->contar os animais p/especie
contagem={}
for chave in animais.keys():
    especie=chave[0]
    #verificar se a especie existe no dicionario
    if especie in contagem:
        contagem[especie]+=1
    else:
        contagem[especie]=1
print(contagem)
    

#->especie e raca do animal mais velho
mais_velho=0
o_mais_velho=None
for chave,valor in animais.items():
    if valor["idade"]>mais_velho:
        mais_velho=valor["idade"]
        o_mais_velho=chave
print(f"O animal mais velho foi {o_mais_velho} com a idade de {mais_velho}")

#media de idades dos animais 
soma=0
for valor in animais.values():
    soma=soma+valor["idade"]
media=soma/len(animais)
print(f"A media das idades dos animais é de {media}")    

#mostrar os animais com idade superior à média
for chave, valor in animais.items():
    if valor["idade"]>media:
        print(f"Animal com idade superior à média {chave}")

#mostrar percentagem de animais por especie
for chave, valor in contagem.items():
    percentagem=valor/len(animais)*100
    print(f"A especie {chave} representa {percentagem}% de animais")

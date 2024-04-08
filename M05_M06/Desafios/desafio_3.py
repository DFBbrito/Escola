'''
PSI - Módulo 5
Estruturas de Dados Compostas
Coleções
'''

# Estrutura de dados
Disciplina_PSI={
                  'Modulos': ('Algoritmia','Estruturas de Controlo','Funções','Estruturas de Dados Estáticas'),
                  'WebGrafia':{'3wschool.com','github.com/alunosnet','udacity.com'} ,
                  'Aulas':['M1','M1','M1','M2','M2','M3','M3','M4','M4','M4','M4'],
                  'Avaliação':['Teste Escrito','Teste prático','Teste prático','Teste prático'],
                  "Classificaçoes":{}
               }

# Mostrar os sites recomendados para a disciplina (webgrafia)
print(Disciplina_PSI["WebGrafia"])
#ou
for elemento in Disciplina_PSI["WebGrafia"]:
    print(elemento)

print("-"*20)
# Mostrar o nome de um módulo pela posição (pedir ao utilizador)
posiçao=int(input("Qual o módulo (1-4): "))
print(Disciplina_PSI["Modulos"][posiçao-1])

print("-"*20)
# Mostrar as aulas que são dadas num módulo (pedir ao utilizador o nº do módulo)
modulo=int(input("qual o nº modulo:"))
modulo=f'M{modulo}'
aulas=Disciplina_PSI["Aulas"]
for aula in aulas:
    if modulo==aula:
        print(aula)

print("-"*20)
# Mostrar os módulos que tenham determinado conteudo (pedir ao utilizador)
conteudo=input("Diga qual o conteudo:")
modulos=Disciplina_PSI["Modulos"]
for modulo in modulos:
    if conteudo.lower() in modulo.lower():
        print(modulo)

print("-"*20)
# Mostrar os módulo cuja avaliação não é 'Teste Escrito'
avaliacoes=Disciplina_PSI["Avaliação"]
for avaliacao in avaliacoes:
    if avaliacao!="Teste Escrito":
        print(avaliacao)
#ou
testes=[avaliacao for avaliacao in avaliacoes if avaliacao!="Teste Escrito"]
print(testes)

print("-"*20)
# Mostrar o nº de módulos da disciplina
print(len(Disciplina_PSI['Modulos']))

print("-"*20)
# Adicionar mais 5 aulas do módulo M2
print(Disciplina_PSI['Aulas'])
for _ in range(5):
    Disciplina_PSI["Aulas"].append("M2")
print(Disciplina_PSI["Aulas"])
#ou
"""
aulas_novas=["M2","M2","M2","M2","M2"]
print(Disciplina_PSI["Aulas"].extend(aulas_novas))
print(Disciplina_PSI["Aulas"])
"""
#ou
"""
Disciplina_PSI["Aulas"].extend(["M2"]*5)
print(Disciplina_PSI["Aulas"])
"""
print("-"*20)
# Adicionar uma chave nova para classificacoes que deve corresponder a uma lista de 4 notas indicadas pelo utilizador
Disciplina_PSI["Classificaçoes"]=[]
for _ in range(4):
    nota=int(input("Nota:"))
    Disciplina_PSI["Classificaçoes"].append(nota)

print(Disciplina_PSI["Classificaçoes"])
print(Disciplina_PSI)
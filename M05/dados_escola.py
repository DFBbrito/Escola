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
                  'Avaliação':['Teste Escrito','Teste prático','Teste prático','Teste prático']
               }

# Mostrar os sites recomendados para a disciplina (webgrafia)
print(Disciplina_PSI.get("WebGrafia"))

# Mostrar o nome de um módulo pela posição (pedir ao utilizador)
pos=int(input("Diz qual modulo queres ver?:"))
if pos==1:
    print(Disciplina_PSI["Modulos"][0])
elif pos==2:
    print(Disciplina_PSI["Modulos"][1])
elif pos==3:
    print(Disciplina_PSI["Modulos"][2])
elif pos==4:
    print(Disciplina_PSI["Modulos"][3])

# Mostrar as aulas que são dadas num módulo (pedir ao utilizador o nº do módulo)
pos=int(input("diga qual o modulo:"))
M=f'M{pos}'
for pos in range(len(Disciplina_PSI['Aulas'])):
    if Disciplina_PSI['Aulas'][pos]==M:
        print(Disciplina_PSI['Aulas'][pos])

# Mostrar os módulos que tenham determinado conteudo (pedir ao utilizador)
conteudo=input("Diga qual o conteudo:")

# Mostrar os módulo cuja avaliação não é 'Teste Escrito'


# Mostrar o nº de módulos da disciplina

# Adicionar mais 5 aulas do módulo M2

# Adicionar uma chave nova para classificacoes que deve corresponder a uma lista de 4 notas indicadas pelo utilizador
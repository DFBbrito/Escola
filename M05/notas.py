turma={
    123:{'M01':10,"M02":15,"M03":8},
    124:{"M01":10,"M02":15,"M03":18},
    125:{"M01":12,"M02":11,"M03":10}
}

#Mostrar as notas dos alunos, primeiro deve mostrar o nº processo e depois a nota de cada modulo
print("Informaçoes aluno")
print("="*10)
for nprocesso,notas in turma.items():
    print(f"{nprocesso=}")
    for modulo,nota in notas.items():
        print(f" {modulo=} - {nota=}")
    print("-"*12)

#calcular e mostrar a média das notas por aluno
print("Média por aluno")
print("="*10)
for nprocesso,notas in turma.items():
    notas_alunos=notas.values()
    media=sum(notas_alunos)/len(notas_alunos)
    print(f"{nprocesso=} - A média é {media:.0f}")
print("-"*12)

#Calcular e mostrar o nº de positivos e negativos por aluno
print("Positiva e Negativa por aluno")
print("="*10)
for nprocesso,notas in turma.items():
    notas_aluno=notas.values()
    positivas=0
    for nota in notas_aluno:
        if nota >=10:
            positivas+=1
    print(f"{nprocesso=}\n-> positivas={positivas}\n-> negativas={len(notas_aluno)-positivas}")
    print("-"*12)

#calcular e mostrar qual o aluno com melhor média
print("Melhor aluno")
print("="*10)
melhor=0
for nprocesso,notas in turma.items():
    notas_alunos=notas.values()
    media=sum(notas_alunos)/len(notas_alunos)
    if media>melhor:
        melhor=media
        melhor_nprocesso=nprocesso
print(f"{melhor_nprocesso=}\n-> melhor média={melhor:.2f}")





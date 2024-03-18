"""
Crie um programa para guardar os dados de uma turma de alunos: precisamos de guardar os nomes, as notas e as faltas dos alunos. O programa deve ler esses dados do utilizador e depois mostrar o nome dos alunos que conseguiram obter aprovação, para isso o aluno deve ter nota superior ou igual a 10 e no máximo 10 faltas.
"""
import numpy as np

names = np.zeros(10, dtype=object)
grades = np.zeros(10, dtype=int)
faults = np.zeros(10, dtype=int)

for i in range(10):
    name = input("Introduza o nome do aluno: ")
    names[i] = name
    grade = int(input("Introduza a nota do aluno: "))
    grades[i] = grade
    faults[i] = int(input("Introduza as faltas do aluno: "))

approved = []

for i in range(10):
    if grades[i] >= 10 and faults[i] <= 10:
        approved.append(names[i])

print("Alunos aprovados: ", approved)
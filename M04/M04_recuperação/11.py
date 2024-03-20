"""
Altere o programa anterior para mostrar o nome do aluno com a melhor nota.
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

max_grade = np.max(grades)

for i in range(10):
    if grades[i] == max_grade:
        print("Aluno com a melhor nota: ", names[i])
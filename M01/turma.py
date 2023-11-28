n= int(input("Quantos alunos têm a turma: "))

c_posistivas = 0
c_negativas = 0

for i in range(0,n):
    nota= int(input("Notas dos alunos de 0 a 20: "))
    if nota>=10:
        print("Positiva")
        c_posistivas = c_posistivas+1
        if nota==20:
            print("Excelente")
            
    elif nota<10:
        print("Negativa")
        c_negativas = c_negativas +1
else:
    if nota==0:
        print("Reprovado")
print("A turma têm %d postivas\nA turma têm %d negativas"%(c_posistivas,c_negativas))

soma = c_negativas+c_posistivas

media = soma/n

print("A media da turma é",media)
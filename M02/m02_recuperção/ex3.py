lugares=150
número_turmas=0
while lugares!=0:
    n_alunos=int(input("quantos alunos são:"))
    if n_alunos==0:
        break
    if n_alunos>lugares:
        print('Não há lugares')
    else:
        lugares-=n_alunos
        número_turmas+=1
    print(f'{número_turmas}{lugares}')

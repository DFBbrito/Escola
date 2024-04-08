"""
Crie um tuplo com os nomes dos meses do ano 
"""
meses=("janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro")

"""
Imprima o terceiro mês do ano
"""
print(meses[2])

"""
Obtenha o tuplo dos meses de verão 
"""
verao=meses[5:8]

"""
Verifique se "Junho" está presente no tuplo de meses
"""
if "junho" in meses:
    print("esta presente")
else:
    print("n esta presente")

"""
Concatene dois tuplos de cores
"""
cores_primarias=("Vermelho","Verde","Azul")
cores_secundarias=("Laranja","Violeta","Amarelo")

cores=cores_primarias+cores_secundarias

print(cores)

"""
Repita o tuplo de cores 3 vezes
"""
cores_3=cores*3

print(cores_3)

"""
Crie um tuplo com 5 elementos, onde o primeiro e o ultimo sao iguais
"""
t_n=(1,2,3,4,1)

"""
Encontre o indice da primeira ocorrencia de "verde" na tupla de cores
"""
pos=cores.index("Verde")
print(pos)

"""
Conte quantas vezes a letra "a" aparece na tupla de palavras 
"""
palavras=("bia","maria","adues")
soma=0
for elemento in palavras:
    n=elemento.count('a')
    soma+=n
print(soma)

"""
Ordene um tuplo de numeros em ordem crescente
"""
num=(33,21,10,-5)
num_ord=sorted(num)

print(num_ord)

###Hacker###
"""
Crie uma funçao que recebe um tuplo de numeros e retorna a soma de todos os elementos 
"""
def Numeros(num):
    x=num[0]+num[1]+num[2]
    return x

num=(50,50,100)
print(Numeros(num))

"""
Crie uma funçao que recebe um tuplo de palavras e retorna a palavra mais longa 
"""
def Palavras(nomes):
    maior=max(nomes)
    return maior

nomes=("Daniel","Frederico","Antonio","Jubileu Galileu")
print(Palavras(nomes))

"""
Escreva um programa que lê um tuplo de numeros do usuario e imprime a média dos numeros pares
"""

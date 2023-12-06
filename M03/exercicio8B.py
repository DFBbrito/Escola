"""
"""
import exercicio8A
import sys

#Ler os valores dos parametros da linha do comandos
if len(sys.argv)!=3:
    print("erro!. Tem de indicar 2 valores. Por exemplo: python exercicio8A.py 10 5")
    sys.exit()

n1=int(sys.argv[1])
n2=int(sys.argv[2])

#calcular.e.mostrar.o. MDC
exercicio8A.MDC(n1,n2)

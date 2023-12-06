"""
"""
import sys

if len(sys.argv) != 3:
    print("Erro! Tem de indicar 2 argumentos. Por exemplo:python linha_comandos 10 5")
    sys.exit()

for valores in sys.argv:
    print(valores)

primeiro_argumento=sys.argv[1]
segundo_argumento=sys.argv[2]
print(primeiro_argumento, segundo_argumento)

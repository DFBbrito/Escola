#Daniel Brito#
"""
Escreve uma funçao que, recebe como parâmetros de entrada as medidas dos dois catetos de um triângulo rêtangulo,
e devolva a medida da hipotenusa.
"""
import math
def Hipotenusa(c1,c2):
    hip=math.sqrt(c1**2)+(c2**2)
    return hip

print(Hipotenusa(2,2))
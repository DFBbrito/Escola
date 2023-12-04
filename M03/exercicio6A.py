#Daniel Brito
"""
funçao que calcule a distancia entre dois pontos no plano cartesiano
"""
import math

def DistanciaDoisPontos(x1,y1,x2,y2):
    c1=x2-x1
    c2=y2-y1
    d=math.sqrt(c1**2+c2**2)
    print(d)

def main():
    DistanciaDoisPontos(1,2,4,6)

if __name__ == "__main__":
    main()
"""
uma funçao que encontre o maximo divisor comum (MDC) entre dois numeros
"""
def MDC(x1,x2):
    if x1<x2:
        menor=x1
    else:
        menor=x2
    for i in range(menor,0,-1):
        if x1%i==0 and x2%i==0:
            print(i)
            return
        
def main():
    x1=int(input('Diga um nº: '))
    x2=int(input('Diga um nº: '))
    MDC(x1,x2)

if __name__ == "__main__":
    main()
    
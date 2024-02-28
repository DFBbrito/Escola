"""
max_items=20
distancias |                    |

D_apuramento
C_Nulos
A_apuramento
constante maior-menor<50
"""
import numpy as np

Max_Items=20
distancias=np.empty(Max_Items)
n_saltos=0

#ler dados
while True:
    temp=int(input("Distância do salto:"))
    if temp<0:
        break
    distancias[n_saltos]=temp
    n_saltos+=1
    if n_saltos==20:
        break

#marca para apuramento
marca_apuramento=int(input("Qual a marca para o apuramento?:"))

#saltos apurados
str_apurados=""
for i in range(n_saltos):
    if distancias[i]>marca_apuramento:
        str_apurados+= f"Nº{i+1}, "

#maior e menor
maior_distancia=distancias[0]
menor_distancia=10000 #nº impossivel de atingir e nao pode ser 0
for i in range(n_saltos):
    if distancias[i]>maior_distancia:
        maior_distancia=distancias[i]
    if distancias[i]>0 and distancias[i]<menor_distancia:
        menor_distancia=distancias[i]
diferença=maior_distancia-menor_distancia
if diferença<50:
    print("prova constante")
else:
    print("prova inconstante")

#saltos nulos
contar_saltos_nulos=0    
for i in range(n_saltos):
    if distancias[i]==0:
        contar_saltos_nulos+=1
print(f"Nº de saltos nulos: {contar_saltos_nulos}")
print(f"Atletas apurados para a final {str_apurados}")
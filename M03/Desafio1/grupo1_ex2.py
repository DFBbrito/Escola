"""
Correção
"""
n1 = float(input('um numero: '))
n2 = float(input('um numero: '))
n3 = float(input('um numero: '))

if n1>=n2 and n1>=n3:
    print(n1)
if n2>=n1 and n2>=n3:
    print(n2)
if n3>=n1 and n3>=n2:
    print(n3)

#mais eficiente
if n1>=n2 and n2>=n3:
    print(n1)
elif n2>=n3:
    print(n2)
else:
    print(n3)

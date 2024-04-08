import numpy as np

email=input("diga o seu email:")
passward=input("digite a passe")

def validar(passward):
    if passward in email:
        return "esta invalida"
    if len(passward)<8:
        return "esta invalida"
    elif passward is passward.lower() and passward.upper():
        return "esta invalida"
    elif passward is passward.isdigit():
        return "esta invalida"
    return "Esta correta"

print(validar(passward))
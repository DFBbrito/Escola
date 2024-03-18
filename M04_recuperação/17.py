"""
Uma palavra-passe é considerada forte se tiver letras, maiúsculas e minúsculas, números e carateres especiais. Crie uma função que indica se uma palavra passe é ou não forte
"""
import string

def is_strong_password(password):
    if len(password) < 8:
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in string.punctuation for c in password):
        return False
    return True

print(is_strong_password("Teste123")) # False
print(is_strong_password("Teste123!")) # True
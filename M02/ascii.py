#Daniel Brito#
"""
Tabela ASCII
"""
letra = input('letra do alfabeto: ')
ascii_code = ord(letra)
print(ascii_code)

# carater correspondente ao codigo ASCII
for i in range(255):
    print(chr(i))

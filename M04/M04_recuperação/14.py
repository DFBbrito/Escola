"""
Crie um programa para sortear os números do euro milhões. Devemos sortear 5 números entre 1 e 50 e mais 2 números entre 1 e 12. Os números sorteados não se podem repetir. Devemos mostrar os números por ordem crescente.
"""
import numpy as np

numbers = np.zeros(7, dtype=int)

for i in range(5):
    number = np.random.randint(1, 51)
    while np.any(numbers == number):
        number = np.random.randint(1, 51)
    numbers[i] = number

for i in range(5, 7):
    number = np.random.randint(1, 13)
    while np.any(numbers == number):
        number = np.random.randint(1, 13)
    numbers[i] = number

numbers = np.sort(numbers)
print("Números sorteados: ", numbers)
"""
Um senhor Joaquim precisa de um programa para ajudar a gerir a fila de espera dos seus clientes. O programa deve permitir inserir o nome do cliente num array. O programa deve mostrar os clientes em espera por ordem de chegada. Sempre que um cliente é atendido deve ser retirado da lista de espera. No máximo podem estar 10 clientes à espera.
"""
import numpy as np

names = np.zeros(10, dtype=object)

def add_client(name):
    for i in range(10):
        if names[i] == "":
            names[i] = name
            break

def remove_client():
    for i in range(9, -1, -1):
        if names[i] != "":
            names[i] = ""
            break

def list_clients():
    for i in range(10):
        if names[i] != "":
            print("Cliente ", i+1, ": ", names[i])

add_client("João")
add_client("Maria")
add_client("Pedro")
add_client("Ana")
add_client("José")

list_clients()

remove_client()

list_clients()
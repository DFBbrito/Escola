"""
Fazer um programa para gerir os contactos de uma agenda. Deve permitir adicionar nome e telefone de cada contacto. Deve permitir listar todos e pesquisar por um nome. Deve permitir Alterar o telefone de um nome.
"""
import numpy as np

contacts = np.zeros((10, 2), dtype=object)

def add_contact(name, phone):
    for i in range(10):
        if contacts[i][0] == "":
            contacts[i][0] = name
            contacts[i][1] = phone
            break

def list_contacts():
    for i in range(10):
        if contacts[i][0] != "":
            print("Nome: ", contacts[i][0], " - Telefone: ", contacts[i][1])

def search_contact(name):
    for i in range(10):
        if contacts[i][0] == name:
            print("Nome: ", contacts[i][0], " - Telefone: ", contacts[i][1])

def change_phone(name, phone):
    for i in range(10):
        if contacts[i][0] == name:
            contacts[i][1]= phone
            break

add_contact("João", "912345678")
add_contact("Maria", "923456789")
add_contact("Pedro", "934567890")
add_contact("Ana", "945678901")
add_contact("José", "956789012")

list_contacts()

search_contact("Pedro")

change_phone("Maria", "929876543")

list_contacts()
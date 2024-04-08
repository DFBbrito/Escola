#ex1
"""Faça um programa que leia o nome e a média de um aluno, guardando também a sua situação (APROVADO/REPROVADO) num dicionário. No final, mostre o conteúdo da estrutura no ecrã."""

nome=input("Nome:")
media=float(input("Media:"))
situaçao="Aprovado" if media>=10 else "Reprovado"

aluno={"Nome":nome,"Media":media,"Situaçao":situaçao}

print(aluno)


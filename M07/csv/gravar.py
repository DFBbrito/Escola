import csv

dados = [
    {"nome":'Joaquim',
     "idade":33,
     "cidade":'Viseu'},
    {"nome":'Antonio',
     "idade":28,
     "cidade":'Lisboa'},
    {"nome":'Maria',
     "idade":21,
     "cidade":'Faro'}
]

with open("dados.csv","w",encoding="utf-8",newline="") as ficheiro:
    #cabdçalho
    campos=dados[0].keys()
    escritor=csv.DictWriter(ficheiro,campos)
    escritor.writeheader()
    for dado in dados:
        escritor.writerow(dado)

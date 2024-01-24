def deposito(valor,taxa,anos):
    valor_deposito=valor

    for i in range(anos):
        juros=valor_deposito*taxa/100
        valor_deposito+=juros
        print(valor_deposito)
    
    return valor_deposito-valor

print(deposito(5000,3,5))
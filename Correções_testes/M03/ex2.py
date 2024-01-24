def signo(mes,dia):
    if (mes==3 and dia>=21) or (mes==4 and dia<=20):
        return "Aries"
    elif (mes==4 and dia>=21) or (mes==5 and dia<=20):
        return "Touro"
    #....resto dos signos
    else:
        return "Data Inválida"
    
print(signo(1,1))

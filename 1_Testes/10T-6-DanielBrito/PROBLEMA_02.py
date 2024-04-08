#Daniel Brito
def signos(d,m):
    if d<=0 or d>31:
        return ("Data incorreta!")
    elif m<=0 or m>12:
        return ("Data incorreta!")
    elif (d>=21 and m==3) and (d<=20 and m==4):
        return ("Áries")
    elif (d>=21 and m==4) and (d<=20 and m==5):
        return ("Touro")
    elif (d>=21 and m==5) and (d<=20 and m==6):
        return ("Gémeos")
    elif (d>=21 and m==6) and (d<=21 and m==7):
        return ("Câncer")
    elif (d>=22 and m==7) and (d<=22 and m==8):
        return ("Leão")
    elif (d>=23 and m==8) and (d<=22 and m==9):
        return ("Virgem")
    elif (d>=23 and m==9) and (d<=22 and m==10):
        return ("Libra")
    elif (d>=23 and m==10) and (d<=21 and m==11):
        return ("Escorpiao")
    elif (d>=22 and m==11) and (d<=21 and m==12):
        return ("Sagitario")
    elif (d>=22 and m==12) and (d<=20 and m==1):
        return ("Capricórnio")
    elif (d>=21 and m==1) and (d<=19 and m==2):
        return ("Aquário")
    elif (d>=20 and m==2) and (d<=20 and m==3):
        return ("Peixes")

print(signos(12,2))
print(signos(30,13))
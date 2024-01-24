def converte(tempo_seg):
    texto_convertido=""
    m=tempo_seg//60
    s=tempo_seg%60
    if m>=10:
        texto_convertido=str(m)+":"
    else:
        texto_convertido="0"+str(m)+":"
    if s>=10:
        texto_convertido+=str(s)
    else:
        texto_convertido+="0"+str(s)
    return texto_convertido

print(converte(125))
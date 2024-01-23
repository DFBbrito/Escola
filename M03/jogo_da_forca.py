def jogo_da_forca(palavra_oculta):
    # Inicialize variáveis necessárias (como lista para o progresso, número de tentativas, etc.)
    letras_corretas = set(palavra_oculta)
    letras_descobertas = set()
    tentativas_maximas = 6

    # Implemente a lógica do jogo, permitindo que o usuário faça tentativas
    while tentativas_maximas > 0 and letras_corretas != letras_descobertas:
        tentativa = input("Digite uma letra: ")

        if tentativa in letras_corretas:
            letras_descobertas.add(tentativa)
            print("Letra correta!")
        else:
            tentativas_maximas -= 1
            print(f"Letra incorreta! Tentativas restantes: {tentativas_maximas}")

    # Forneça feedback sobre o resultado
    if letras_corretas == letras_descobertas:
        print(f"Parabéns! Você descobriu a palavra: {palavra_oculta}")
    else:
        print(f"Game over! A palavra era: {palavra_oculta}")


# Exemplo de chamada:
palavra = "python"
jogo_da_forca(palavra)

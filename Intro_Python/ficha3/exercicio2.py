def contar_caracteres(texto):
    contagem = {}
    for caractere in texto:
        if caractere in contagem.keys():
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
    return contagem

resultado = contar_caracteres("Programação")
print(resultado)
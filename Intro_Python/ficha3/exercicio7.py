texto = input("Escreva alguma coisa para analisar: ")

pontuacao = ".,!?;:-_()[]{}\"'*/\\"
texto_limpo = ""
for c in texto.lower():
    if c not in pontuacao:
        texto_limpo += c

palavras = texto_limpo.split()

frequencias = {}
for palavra in palavras:
    if palavra in frequencias:
        frequencias[palavra] += 1
    else:
        frequencias[palavra] = 1

ordenadas = sorted(frequencias.items(), key=lambda item: item[1], reverse=True)
top5 = ordenadas[:5]

total_palavras = len(palavras)
palavras_unicas = len(frequencias)
comprimento_total = 0
for p in palavras:
    comprimento_total += len(p)
comprimento_medio = round(comprimento_total / total_palavras, 2) if total_palavras > 0 else 0

analise = {
    "total_palavras": total_palavras,
    "palavras_unicas": palavras_unicas,
    "comprimento_medio": comprimento_medio,
    "palavras_mais_comuns": dict(top5)
}

print("\nRESULTADOS DA ANÁLISE DE TEXTO ")
print(f"Total de palavras: {analise['total_palavras']}")
print(f"Palavras únicas: {analise['palavras_unicas']}")
print(f"Comprimento médio das palavras: {analise['comprimento_medio']}")
print("\npalavras mais comuns:")
for palavra, freq in analise["palavras_mais_comuns"].items():
    print(f"{palavra}: {freq}")
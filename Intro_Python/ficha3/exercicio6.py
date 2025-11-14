estudantes = {"Ana": 18, "Carlos": 15, "Bruno": 17, "Diana": 19, "Eva": 14}

ordenado_por_nome = dict(sorted(estudantes.items()))
print("Ordenado por nome (chave):")
print(ordenado_por_nome)

ordenado_por_nota = dict(sorted(estudantes.items(), key=lambda item: item[1], reverse=True))
print("\nOrdenado por nota (valor) decrescente:")
print(ordenado_por_nota)

def ordenar_dicionario(dicionario, por="chave", reverso=False):
    if por == "chave":
        return dict(sorted(dicionario.items(), key=lambda item: item[0], reverse=reverso))
    elif por == "valor":
        return dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=reverso))
    else:
        raise ValueError("O parâmetro 'por' deve ser 'chave' ou 'valor'.")

print("\nFunção - ordenado por chave:")
print(ordenar_dicionario(estudantes, por="chave"))

print("\nFunção - ordenado por valor (decrescente):")
print(ordenar_dicionario(estudantes, por="valor", reverso=True))
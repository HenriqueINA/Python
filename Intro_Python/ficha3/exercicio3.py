biblioteca = {
    "livro1": {
        "titulo": "Python Fluente",
        "autor": "Luciano Ramalho",
        "ano": 2015,
        "disponivel": True
    },
    "livro2": {
        "titulo": "Pense em Python",
        "autor": "Allen B. Downey",
        "ano": 2012,
        "disponivel": False
    },
    "livro3": {
        "titulo": "Introdução à Programação com Python",
        "autor": "Nilo Ney Coutinho Menezes",
        "ano": 2019,
        "disponivel": True
    }
}

print("Livros disponíveis:")
for livro in biblioteca.values():
    if livro["disponivel"]:
        print(f"- {livro['titulo']}")

# Novo livro da biblioteca
biblioteca["livro4"] = {
    "titulo": "abc",
    "autor": "Henrique",
    "ano": 2015,
    "disponivel": True
}

# Livro 1 indisponível
biblioteca["livro1"]["disponivel"] = False

# Livros do autor
def livros_por_autor(nome_autor):
    titulos = []
    for livro in biblioteca.values():
        if livro["autor"] == nome_autor:
            titulos.append(livro["titulo"])
    return titulos

autor = "Luciano Ramalho"
print(f"\nLivros do autor '{autor}':")
print(livros_por_autor(autor))
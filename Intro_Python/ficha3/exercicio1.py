aluno = {
    "nome": "Ana Silva",
    "idade": 17,
    "disciplinas": ["Matemática", "Física", "Informática"],
    "notas": {"Matemática": 18, "Física": 17, "Informática": 19}
}

aluno["disciplinas"].append("Português")
aluno["notas"]["Português"] = 16

aluno["disciplinas"].append("Português")
aluno["notas"]["Português"] = 16

notas_aluno = ["notas"]
notas = [nota for nota in notas_aluno.values()]
media = sum(notas) / len(notas)
print(f"Média das notas: {media:.2f} valores")
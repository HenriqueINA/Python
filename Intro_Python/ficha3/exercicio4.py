quadrados = {num: num**2 for num in range(1, 11)}
print("1. Quadrados de 1 a 10:")
print(quadrados)

palavras = ["banana", "casa", "felicidade", "sol", "computador"]
comprimentos = {palavra: len(palavra) for palavra in palavras}
print("\n2. Comprimentos das palavras:")
print(comprimentos)

notas = {"Ana": 18, "Bruno": 15, "Carla": 17, "David": 12, "Eva": 19}
aprovados = {aluno: nota for aluno, nota in notas.items() if nota >= 15}
print("\n3. Alunos com notas maiores ou iguais a 15:")
print(aprovados)
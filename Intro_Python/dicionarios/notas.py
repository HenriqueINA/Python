notas = {
    'sergio': {'matematica': 13.25, 'programacao': 17.75, 'outras': [12.25, 13.50, 17]},
    'goncalo': {'matematica': 14.25, 'programacao': 12.50, 'outras': [11.25, 14, 15.50]},
    'renan': {'matematica': 16.25, 'programacao': 13.75, 'outras': [13, 17.50, 20]},
    'tomas': {'matematica': 8.25, 'programacao': 15, 'outras': [7, 12.50, 14.75]}
}

# Imprimir a nota de matemática do Gonçalo
print(notas['goncalo']['matematica'])

# Imprimir a maior nota de matemática
maior_nota = 0
for k in notas.keys():
    if notas[k]['matematica'] > maior_nota:
        maior_nota = notas[k]['matematica']
print(maior_nota)

# Imprimir a maior nota de matemática (List Comprehension)
print(max([notas[k]['matematica'] for k in notas.keys()]))

# Nova nota em outras disciplicas para o Tomás
notas['tomas']['outras'].append(16.25)
print("Média das outras disciplinas do Tomás: ")
print(f"{sum(notas['tomas']['outras']) / len(notas['tomas']['outras'])}")

# Imprimir o aluno com maior nota de programação
maior_nota = 0
melhor_aluno = ""
for k in notas.keys():
    if notas[k]['programacao'] > maior_nota:
        melhor_aluno = k
print(melhor_aluno)
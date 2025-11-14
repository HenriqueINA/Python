import os

aluno = {
    'nome': 'Henrique Oliveira',
    'naturalidade': 'Portugal',
    'peso': 56,
    'altura': 1.75,
    'aprovado': True
}

# Imprimir uma chave do dicionário
print(aluno['naturalidade']) # Portugal
print(f"O aluno {aluno['nome']} tem de peso {aluno['peso']}kg.")

# Características do aluno
for chave in aluno.keys():
    print (chave)

# Valores das chaves
for v in aluno.values(): print(v)

# Par chave/valor
for k, v in aluno.items():
    print(f"{k}: {v}")
    
# aluno['imc'] = round(aluno['peso'] / (aluno['altura'] * aluno['altura']),2)
# aluno['naturalidade'] = 'Itália'
# os.system("cls")
# print(aluno)

d = { }
d = dict() # Dicionário vazio
d1 = dict(nome="Henrique",idade=16)
d2 = {'nome':'Henrique', 'idade':16}
d = dict([('nome','Henrique'),('idade', 16)])

d1['idade'] = 17
idade = d1.get('idade2')
print(idade)

for chave in d2.keys():
    print(chave) # nome, idade
for v in d2.values():
    print(v) # Henrique, 16
for c,v in d2.items():
    print(f"{c} com valor {v}")
    
produtos = {
    'casaco': {'preco': 23.99, 'iva': 0.23},
    'camisa': {'preco': 71.99, 'iva': 0.13},
    'sapato': {'preco': 55.99, 'iva': 0.23}
}    
# exercicio 1 
lista = []

for i in range(1,11):
    lista.append(i)
       
dobro = [i*2 for i in lista]
print(dobro)

# exercicio 2   
quadrado = [i**2 for i in lista]
print(quadrado)

# exercicio 3
lista_nomes = ['Henrique', 'André', 'Marcelo']
tamanho_nomes = [len(i) for i in lista_nomes]
print(tamanho_nomes)
  
# exercicio 5
nome = 'HenrIque SilvA OlivEira'
maiusculas = [letra for letra in nome if letra.isupper()]
print(maiusculas)

# exercicio 6
numeros = [1, 3, 4, 6, 7, 9, 10]
nova_lista = [num * 2 if num % 3 == 0 else num for num in numeros]
print(nova_lista)

#exercicio 7
nomes = ['Ana', 'Bruno', 'Amanda', 'Carlos', 'Alex', 'Beatriz']
nomes_com_a = [nome.upper() for nome in nomes if nome.startswith('A')]
print(nomes_com_a)

#exercicio 8
frutas = ['banana', 'uva', 'abacaxi', 'pera', 'laranja']
nova_lista = [len(fruta) if len(fruta) > 5 else 0 for fruta in frutas]
print(nova_lista)
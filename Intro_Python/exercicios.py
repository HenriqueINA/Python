# Exercicio 01
# Crie um programa que peça o comprimento e a largura
# de um retangulo e mostre a area e o perimetro

# num1 = input("Digite o comprimento: ")
# num2 = input("Digite a largura: ")
# perimetro = num1 + num2
# area = num1 * num2

# print(f'O perímetro do retângulo é: ', perimetro)
# print(f'A área do retângulo é: ', area)

# Exercicio 02
# Crie uma lista com 10 nums e imprima apenas os numeros pares

# nums = [1,2,3,4,5,6,7,8,9,10]

# for i in nums:
#   if i % 2 == 0: print(i)

# Exercicio 03
# Crie um dicionario em que as chaves sejam nomes de produtos.
# Os valores sejam os preços de cada produto.
# Deve devolver o produto mais caro e a media dos preços.

produtos = {"Madeira": 4.90, "Tijolo": 10.00, "Metal": 50.24}
soma = 0
preco_mais_caro = 0
produto_mais_caro = ""
for nome_produto, preco in produtos.items():
    soma = soma + preco
    if preco > preco_mais_caro:
        preco_mais_caro = preco
        produto_mais_caro = nome_produto
        
media = soma / len(produtos)
print(f"O produto mais caro é {produto_mais_caro}")
print(f"Média dos preços = {media:.2f}€")

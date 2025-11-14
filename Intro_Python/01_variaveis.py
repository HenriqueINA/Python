# x = 5
# print(x)
# print(type(x))
# x = "Henrique"
# print(x)
# print(type(x))
# a,b,c = "Riczão", 123, True
# print(a,b,c)

num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
soma = num1 + num2
media = (num1+num2) / 2

#print("a soma de ", num1, " com ", num2, " é ", soma)
#print("a soma de ", str(num1), " com ", str(num2), " é ", str(soma))

# fstring
print(f'a soma de {num1} com {num2} é igual a {soma:.2f}')
print(f'a média de {num1} com {num2} é igual a {media:.2f}')
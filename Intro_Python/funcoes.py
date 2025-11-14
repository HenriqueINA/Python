def saudacao(nome):
    print(f"Olá, {nome}!")
    
saudacao("Maria")    
saudacao(None)

def frase(nome, idade=18, peso=60):
    print(f"O(A) {nome} tem {idade} anos e pesa {peso}kg.")
frase("Henrique", 16, 55)
frase("João")

def listar_nomes(*args):
    for nome in args:
        print(nome, end="")
        
def listar_lista_nomes(lista):
    for nome in lista:
        print(nome, end="")
        
# listar_nomes("Henrique", "Ana")
# print()
# listar_nomes("João", "José", "Carlos", "Rui", "Maria")
# listar_nomes(["Rui", "Linda", "Moura"])

def listar_dados(**kwargs):
    for chave, dado in kwargs.items():
        print(f"{chave}: {dado}")

listar_dados(nome="Henrique", idade=16, peso=55)

# Função anónima
somar = lambda x,y: x+y
print(somar(2,3))

lista=[1,2,3,4,5]
segundo_elemento = lambda x: x[1]
print(segundo_elemento(lista))
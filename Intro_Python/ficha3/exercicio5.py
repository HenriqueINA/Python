import os, getpass
from inventario import adicionar, atualizar, remover, abaixo_do_stock, valor_total

def menu():
    print("1 - Adicionar produto")
    print("2 - Atualizar quantidade")
    print("3 - Remover produto")
    print("4 - Listar produtos abaixo do stock")
    print("5 - Valor em stock")
    print("6 - Listar dicionario de produtos")
    print("7 - Sair")
    escolha = int(input("Digite a opção a ser executada: "))
    return escolha

inventario = {}
op = menu()

while op < 7:
    if op == 1:
        inventario = adicionar(inventario)   
    elif op == 2:
        qtde = int(input("Quantidade atualizada: "))
        inventario = atualizar(inventario, qtde)
    elif op == 3:
        inventario = remover(inventario)
    elif op == 4:
        qtde = int(input("Quantidade considerada abaixo do stock: "))
        inventario = abaixo_do_stock(inventario)
    elif op == 5:
        print(f"Valor em stock: {valor_total(inventario)}")
    elif op == 6:
        print(inventario)
    else:
        break
    getpass.getpass("Pressione ENTER para voltar ao menu")
    os.system("cls")
    op = menu()
    
print("Programa terminado")
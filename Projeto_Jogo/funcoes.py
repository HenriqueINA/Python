import os
import pickle

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_capa():
    print("#################################")
    print("####  BATALHA DE NAVES  #########")
    print("#################################\n")

def menu_principal():
    print("1. Iniciar Jogo")
    print("2. Carregar Jogo")
    print("3. Guardar Jogo")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def salvar_jogo(arquivo, dados):
    with open(arquivo, "wb") as f:
        pickle.dump(dados, f)
    print("Jogo salvo com sucesso!")

def carregar_jogo(arquivo):
    try:
        with open(arquivo, "rb") as f:
            dados = pickle.load(f)
        print("Jogo carregado com sucesso!")
        return dados
    except FileNotFoundError:
        print("Nenhum jogo encontrado!")
        return None
import random

def criar_tabuleiro(linhas=5, colunas=5):
    """Cria um tabuleiro vazio de dimensões linhas x colunas."""
    return [[" " for _ in range(colunas)] for _ in range(linhas)]

def imprimir_tabuleiro(tabuleiro):
    """Imprime o tabuleiro na tela."""
    for linha in tabuleiro:
        print(" | ".join(linha))
    print()

def colocar_naves(tabuleiro, naves):
    """Coloca as naves aleatoriamente no tabuleiro, sem sobreposição."""
    posicoes_usadas = []
    for nave in naves:
        while True:
            x = random.randint(0, len(tabuleiro) - 1)
            y = random.randint(0, len(tabuleiro[0]) - 1)
            if (x, y) not in posicoes_usadas:
                tabuleiro[x][y] = nave.simbolo
                posicoes_usadas.append((x, y))
                break
    return posicoes_usadas

def obter_tiro_manual(tabuleiro, posicoes_usadas):
    """Recebe coordenadas do jogador para um tiro manual e valida entrada."""
    while True:
        try:
            entrada = input("Digite o tiro (linha,coluna): ")
            x_str, y_str = entrada.split(",")
            x = int(x_str.strip())
            y = int(y_str.strip())

            if x < 0 or x >= len(tabuleiro) or y < 0 or y >= len(tabuleiro[0]):
                print("Coordenadas fora do tabuleiro! Tente novamente.")
            elif (x, y) in posicoes_usadas:
                print("Já foi dado tiro nesta posição! Tente outra.")
            else:
                return (x, y)
        except ValueError:
            print("Formato inválido! Digite no formato linha,coluna.")

def exibir_tabuleiros_rodada(tabuleiro_oculto, tabuleiro_tiros, tabuleiro_proxima):
    """Mostra os três tabuleiros ao final de uma rodada."""
    print("\nTabuleiro da rodada anterior (posições das naves):")
    imprimir_tabuleiro(tabuleiro_oculto)

    print("Tabuleiro da rodada anterior (tiros dados):")
    imprimir_tabuleiro(tabuleiro_tiros)

    print("Tabuleiro limpo para próxima rodada:")
    imprimir_tabuleiro(tabuleiro_proxima)
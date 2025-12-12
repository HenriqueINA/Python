from colorama import init, Fore, Style # ignore
init(autoreset=True)

from naves import NaveModelo, NaveEspecial
from tabuleiro import criar_tabuleiro, obter_tiro_manual, colocar_naves, exibir_tabuleiros_rodada
from funcoes import limpar_tela, mostrar_capa, menu_principal, salvar_jogo, carregar_jogo

def jogo():
    # Criação das naves
    nave1 = NaveEspecial("Falcão", "vermelho", 20, "F", 10)
    nave2 = NaveEspecial("Estrela", "azul", 15, "E", 12)
    nave3 = NaveEspecial("Cometa", "verde", 10, "C", 30)

    naves = [nave1, nave2, nave3]

    # Armazena posições de acertos permanentes (X)
    acertos = {}

    tiros_dados = 0
    tiros_certos = 0

    while True:
        # Criar tabuleiros para a rodada
        tabuleiro_visivel = criar_tabuleiro()
        tabuleiro_oculto = criar_tabuleiro()
        tabuleiro_tiros = criar_tabuleiro()

        # Posicionar naves aleatoriamente
        posicoes_naves = colocar_naves(tabuleiro_oculto, naves)

        # Mostrar acertos anteriores no tabuleiro visível
        for pos in acertos:
            x, y = pos
            tabuleiro_visivel[x][y] = "X"

        limpar_tela()
        print("Tabuleiro para jogar:")
        for linha in tabuleiro_visivel:
            print(" | ".join(linha))
        print()

        if tiros_dados >= 105 or all(n.energia == 0 for n in naves):
            print("Fim de jogo!")
            break

        # Inserção de 3 tiros manuais
        posicoes_tiros = []
        for _ in range(3):
            tiro = obter_tiro_manual(tabuleiro_visivel, posicoes_tiros)
            posicoes_tiros.append(tiro)
            x, y = tiro

            # Verificar acerto
            acertou = False
            for nave in naves:
                if tabuleiro_oculto[x][y] == nave.simbolo:
                    nave.perder_energia()
                    tiros_certos += 1
                    tabuleiro_tiros[x][y] = "X"      # Acerto no tabuleiro de tiros
                    tabuleiro_visivel[x][y] = "X"   # Atualiza tabuleiro visível
                    acertos[(x, y)] = "X"           # Salva acerto permanente
                    acertou = True
                    break

            if not acertou:
                tabuleiro_tiros[x][y] = "O"
                tabuleiro_visivel[x][y] = "O"

        tiros_dados += 3

        # Mostrar dados das naves
        print("\nDados das naves:")
        for nave in naves:
            if nave.denominacao == "Falcão":
                print(Fore.RED+nave.mostrar_dados()+Fore.RESET)
            elif nave.denominacao == "Estrela":
                print(Fore.BLUE+nave.mostrar_dados()+Fore.RESET)
            elif nave.denominacao == "Cometa":
                print(Fore.GREEN+nave.mostrar_dados()+Fore.RESET)

        # Mostrar eficácia de tiros
        eficacia = (tiros_certos * 100 / tiros_dados) if tiros_dados else 0
        print(f"Tiros dados: {tiros_dados} | Tiros certeiros: {tiros_certos} | Eficácia: {eficacia:.2f}%\n")

        # Mostrar os 3 tabuleiros da rodada
        exibir_tabuleiros_rodada(tabuleiro_oculto, tabuleiro_tiros)

        input("Pressione Enter para iniciar a próxima rodada...")

def main():
    while True:
        limpar_tela()
        mostrar_capa()
        escolha = menu_principal()
        if escolha == "1":
            jogo()
        elif escolha == "2":
            dados = carregar_jogo("jogo.sav")
            if dados:
                print("Função de carregar ainda precisa integrar o estado do jogo")
                input("Pressione Enter para continuar...")
        elif escolha == "3":
            print("Função de salvar ainda precisa integrar o estado do jogo")
            input("Pressione Enter para continuar...")
        elif escolha == "4":
            print("Saindo do jogo...")
            break

if __name__ == "__main__":
    main()
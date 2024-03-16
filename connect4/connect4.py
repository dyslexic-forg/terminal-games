NUMERO_DE_LINHAS = 6
NUMERO_DE_COLUNAS = 7

X = 'X'
O = 'O'
VAZIO = ' '

def novo_tabuleiro():
    tabuleiro = []
    for i in range(NUMERO_DE_LINHAS):
        linha = []
        for j in range(NUMERO_DE_COLUNAS):
            linha.append(VAZIO)
        tabuleiro.append(linha)
    return tabuleiro

def mostra_tabuleiro(tabuleiro):
    for i in range(NUMERO_DE_COLUNAS):
        print(f"  {i+1} ", end="")
    print()
    print("+" + NUMERO_DE_COLUNAS * "---+")
    for i in range(NUMERO_DE_LINHAS):
        print("|", end="")
        for j in range(NUMERO_DE_COLUNAS):
            print(f" {tabuleiro[i][j]} |", end="")
        print()
        print("+" + NUMERO_DE_COLUNAS * "---+")

def coloca_peca(tabuleiro, coluna, peca):
    coluna -= 1
    for i in range(NUMERO_DE_LINHAS-1, 0, -1):
        if tabuleiro[i][coluna] == VAZIO:
            tabuleiro[i][coluna] = peca
            return True
    return False

DIRECOES = [
    [0, 1], # direita
    [1, 0], # baixo
    [-1, 1], # cima-direita
    [1, 1] # baixo-direita
]

def verifica_vitoria(tabuleiro):
    for i in range(NUMERO_DE_LINHAS):
        for j in range(NUMERO_DE_COLUNAS):
            for di, dj in DIRECOES:
                ni, nj = i, j
                if tabuleiro[ni][nj] != VAZIO:
                    contador = 1
                    while True:
                        if contador == 4:
                            return (i, j, di, dj)
                        ni += di
                        nj += dj
                        if fora_do_tabuleiro(ni, nj) or tabuleiro[ni][nj] != tabuleiro[i][j]:
                            break
                        contador += 1
    return False

def fora_do_tabuleiro(linha, coluna):
    return linha < 0 or linha >= NUMERO_DE_LINHAS or coluna < 0 or coluna >= NUMERO_DE_COLUNAS

def verifica_empate(tabuleiro):
    if verifica_vitoria(tabuleiro):
        return False
    for coluna in range(NUMERO_DE_COLUNAS):
        if tabuleiro[0][coluna] == VAZIO:
            return False
    return True

def recebe_jogador():
    while True:
        print("Quem começa? [X|O]")
        resp = input("> ").upper()
        if resp == "X" or resp == "O":
            return resp
        print("Escolha inválida.")

def recebe_jogada(tabuleiro, jogador_atual):
    while True:
        print("Escolha uma coluna.")
        resp = input(f"{jogador_atual}> ")
        if resp.isdigit() and len(resp) == 1 and resp >= "1" and resp <= "7":
            result = coloca_peca(tabuleiro, int(resp), jogador_atual)
            if result:
                return
        print("Jogada inválida!")

def proximo_jogador(jogador_atual):
    if jogador_atual == X:
        return O
    return X

def roda_jogo():
    print("Connect 4 para dois jogadores.")
    tabuleiro = novo_tabuleiro()
    jogador_atual = recebe_jogador()
    while True:
        mostra_tabuleiro(tabuleiro)
        recebe_jogada(tabuleiro, jogador_atual)
        if verifica_vitoria(tabuleiro):
            mostra_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break
        if verifica_empate(tabuleiro):
            mostra_tabuleiro(tabuleiro)
            print(f"Empate.")
            break
        jogador_atual = proximo_jogador(jogador_atual)

if __name__ == "__main__":
    roda_jogo()

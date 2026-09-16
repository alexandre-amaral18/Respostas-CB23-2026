
from maze_builder import generate_maze


def dfs_iterativo(maze, inicio):
    pilha = [inicio]
    visitados = set()
    anterior = {inicio: None}

    linhas = len(maze)
    colunas = len(maze[0])

    direcoes = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while pilha:
        atual = pilha.pop()

        if atual in visitados:
            continue

        visitados.add(atual)

        linha, coluna = atual

        if maze[linha][coluna] == '.':
            break

        for dl, dc in direcoes:
            nova_linha = linha + dl
            nova_coluna = coluna + dc

            if not (0 <= nova_linha < linhas and
                    0 <= nova_coluna < colunas):
                continue

            vizinho = (nova_linha, nova_coluna)

            if maze[nova_linha][nova_coluna] == 1:
                continue

            if vizinho in visitados:
                continue

            if vizinho not in anterior:
                anterior[vizinho] = atual

            pilha.append(vizinho)

    return anterior


def encontrar_queijo(maze):
    for linha in range(len(maze)):
        for coluna in range(len(maze[linha])):
            if maze[linha][coluna] == '.':
                return (linha, coluna)

    raise ValueError("Queijo não encontrado no labirinto.")


def reconstruir_caminho(anterior, inicio, objetivo):
    caminho = []
    atual = objetivo

    while atual is not None:
        caminho.append(atual)

        if atual == inicio:
            break

        atual = anterior.get(atual)

    if caminho[-1] != inicio:
        return []

    caminho.reverse()

    return caminho


def mostrar_caminho(maze, caminho):
    labirinto = [linha[:] for linha in maze]

    for linha, coluna in caminho:
        if labirinto[linha][coluna] != '.':
            labirinto[linha][coluna] = '*'

    for linha in labirinto:
        print(" ".join(map(str, linha)))


def resolver_labirinto(maze):
    inicio = (1, 1)

    if not (0 <= inicio[0] < len(maze) and
            0 <= inicio[1] < len(maze[0])):
        raise ValueError("A posição inicial (1, 1) não existe.")

    anterior = dfs_iterativo(maze, inicio)

    queijo = encontrar_queijo(maze)

    caminho = reconstruir_caminho(
        anterior,
        inicio,
        queijo
    )

    return caminho


def main():
    m = 10
    n = 14

    maze = generate_maze(
        m,
        n,
        room=0,
        wall=1,
        cheese='.'
    )

    print("LABIRINTO ORIGINAL")
    print()

    for linha in maze:
        print(" ".join(map(str, linha)))

    caminho = resolver_labirinto(maze)

    print()
    print("CAMINHO ENCONTRADO")
    print()

    if caminho:
        mostrar_caminho(maze, caminho)

        print()
        print("Posição inicial:", caminho[0])
        print("Posição do queijo:", caminho[-1])
        print("Quantidade de posições no caminho:", len(caminho))
    else:
        print("Não foi possível encontrar um caminho.")


if __name__ == "__main__":
    main()

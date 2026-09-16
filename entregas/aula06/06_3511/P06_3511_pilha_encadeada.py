from io import StringIO


class _No:
    """Nó de uma lista simplesmente encadeada."""

    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo


class PilhaEncadeada:
    """Pilha LIFO implementada com lista simplesmente encadeada."""

    def __init__(self):
        """Cria uma pilha vazia em O(1)."""
        self._topo = None
        self._tamanho = 0

    def push(self, item):
        """Insere item no topo da pilha em O(1)."""
        novo_no = _No(item, self._topo)
        self._topo = novo_no
        self._tamanho += 1

    def pop(self):
        """Remove e retorna o topo; lança IndexError se vazia. O(1)."""
        if self._topo is None:
            raise IndexError("não é possível remover de uma pilha vazia")

        valor = self._topo.valor
        self._topo = self._topo.proximo
        self._tamanho -= 1
        return valor

    def topo(self):
        """Retorna o topo sem removê-lo; lança IndexError se vazia. O(1)."""
        if self._topo is None:
            raise IndexError("não é possível consultar o topo de uma pilha vazia")

        return self._topo.valor

    def esta_vazia(self):
        """Retorna True se a pilha estiver vazia. O(1)."""
        return self._tamanho == 0

    def len(self):
        """Retorna a quantidade de elementos da pilha em O(1)."""
        return self._tamanho

    def __repr__(self):
        """Retorna uma representação do topo para a base em O(N)."""
        saida = StringIO()
        saida.write("PilhaEncadeada(")

        atual = self._topo
        primeiro = True

        while atual is not None:
            if not primeiro:
                saida.write(" -> ")

            saida.write(repr(atual.valor))
            primeiro = False
            atual = atual.proximo

        saida.write(")")
        return saida.getvalue()


if __name__ == "__main__":
    pilha = PilhaEncadeada()

    pilha.push(10)
    pilha.push(20)
    pilha.push(30)

    print(pilha)
    print("Topo:", pilha.topo())
    print("Removido:", pilha.pop())
    print("Pilha:", pilha)

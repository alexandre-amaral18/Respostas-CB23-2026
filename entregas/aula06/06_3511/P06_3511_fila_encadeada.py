from P06_3511_pilha_encadeada import PilhaEncadeada
from io import StringIO


class FilaEncadeada:
    """Fila FIFO implementada usando duas pilhas por composição."""

    def __init__(self):
        """Cria uma fila vazia em O(1)."""
        self._entrada = PilhaEncadeada()
        self._saida = PilhaEncadeada()
        self._tamanho = 0

    def _transferir(self):
        """Transfere elementos da pilha de entrada para a saída em O(N)."""
        while not self._entrada.esta_vazia():
            self._saida.push(self._entrada.pop())

    def enfileirar(self, item):
        """Insere item no final da fila em O(1)."""
        self._entrada.push(item)
        self._tamanho += 1

    def desenfileirar(self):
        """Remove e retorna o primeiro item; lança IndexError se vazia.
        
        O custo é O(1) amortizado, embora uma transferência possa custar O(N).
        """
        if self.esta_vazia():
            raise IndexError("não é possível desenfileirar de uma fila vazia")

        if self._saida.esta_vazia():
            self._transferir()

        self._tamanho -= 1
        return self._saida.pop()

    def frente(self):
        """Retorna o primeiro item sem removê-lo; lança IndexError se vazia.
        
        O custo é O(1) amortizado, embora uma transferência possa custar O(N).
        """
        if self.esta_vazia():
            raise IndexError("não é possível consultar a frente de uma fila vazia")

        if self._saida.esta_vazia():
            self._transferir()

        return self._saida.topo()

    def esta_vazia(self):
        """Retorna True se a fila estiver vazia. O(1)."""
        return self._tamanho == 0

    def len(self):
        """Retorna a quantidade de elementos da fila em O(1)."""
        return self._tamanho

    def __repr__(self):
        """Retorna uma representação da frente até o final em O(N)."""
        saida = StringIO()
        saida.write("FilaEncadeada(")
        primeiro = True

        # Elementos que já estão na pilha de saída.
        temporaria_saida = PilhaEncadeada()

        while not self._saida.esta_vazia():
            item = self._saida.pop()
            temporaria_saida.push(item)

            if not primeiro:
                saida.write(" -> ")
            saida.write(repr(item))
            primeiro = False

        while not temporaria_saida.esta_vazia():
            self._saida.push(temporaria_saida.pop())

        # Elementos que ainda estão na pilha de entrada.
        temporaria_1 = PilhaEncadeada()
        temporaria_2 = PilhaEncadeada()

        while not self._entrada.esta_vazia():
            temporaria_1.push(self._entrada.pop())

        while not temporaria_1.esta_vazia():
            item = temporaria_1.pop()
            temporaria_2.push(item)

            if not primeiro:
                saida.write(" -> ")
            saida.write(repr(item))
            primeiro = False

        while not temporaria_2.esta_vazia():
            self._entrada.push(temporaria_2.pop())

        saida.write(")")
        return saida.getvalue()


if __name__ == "__main__":
    fila = FilaEncadeada()

    fila.enfileirar(10)
    fila.enfileirar(20)
    fila.enfileirar(30)

    print(fila)
    print("Frente:", fila.frente())
    print("Removido:", fila.desenfileirar())
    print("Fila:", fila)

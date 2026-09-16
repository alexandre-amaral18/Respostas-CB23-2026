import random
import time
import sys

from AP_03_ordenacao import selection_sort
from AP_03_ordenacao import divide_and_conquer_sort
from AP_03_ordenacao import quick_sort


sys.setrecursionlimit(10000)


def medir_tempo(funcao, lista):
    inicio = time.perf_counter()
    funcao(lista)
    fim = time.perf_counter()
    return fim - inicio


def gerar_caso_medio(n):
    return [random.randint(0, n * 10) for _ in range(n)]


def gerar_pior_caso(n):
    return list(range(n))


def benchmark(algoritmos, tamanhos, repeticoes):
    print(f"{'Algoritmo':<25} {'N':<8} {'Caso':<12} {'Tempo médio (s)':>18}")
    print("-" * 68)

    for nome, funcao in algoritmos:
        for n in tamanhos:
            for caso in ["Médio", "Pior"]:
                tempos = []

                for _ in range(repeticoes):
                    if caso == "Médio":
                        lista = gerar_caso_medio(n)
                    else:
                        lista = gerar_pior_caso(n)

                    tempo = medir_tempo(funcao, lista)
                    tempos.append(tempo)

                media = sum(tempos) / len(tempos)

                print(
                    f"{nome:<25} {n:<8} {caso:<12} {media:>18.8f}"
                )


algoritmos = [
    ("Selection Sort", selection_sort),
    ("Merge Sort", divide_and_conquer_sort),
    ("Quick Sort", quick_sort),
]

tamanhos = [100, 500, 1000, 5000]
repeticoes = 10

benchmark(algoritmos, tamanhos, repeticoes)

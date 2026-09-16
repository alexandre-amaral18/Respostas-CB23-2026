import random
import time
import AulasPraticas.AP_03_ordenacao as ordn
import sys

def calc_medio_pior(f_ord):
    medio = [0.0] * len(Ns)
    pior = [0.0] * len(Ns)

    for i in range(len(Ns)):
        start_time_medio = time.perf_counter()
        f_ord(arrMedio)
        end_time_medio = time.perf_counter()

        start_time_pior = time.perf_counter()
        f_ord(arrPior)
        end_time_pior = time.perf_counter()

        medio[i] += end_time_medio - start_time_medio
        pior[i] += end_time_pior - start_time_pior

        medio[i] /= K
        pior[i] /= K

    return medio, pior

algorithms = [
    "selection_sort",
    "divide_and_conquer_sort",
    "quick_sort",
]

results = {name: calc_medio_pior(getattr(ordn, name)) for name in algorithms}

headers = ["N"] + [f"{tipo} {algo}" for algo in algorithms for tipo in ("Medio", "Pior")]
widths = [15] + [30] * (len(headers) - 1)

print(" | ".join(f"{header:^{width}}" for header, width in zip(headers, widths)))

for i, n in enumerate(Ns):
    row = [f"{n:^15}"]
    for algo in algorithms:
        medio, pior = results[algo]
        row.extend([f"{medio[i]:^30}", f"{pior[i]:^30}"])
    print(" | ".join(row))
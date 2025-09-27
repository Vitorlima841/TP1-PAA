import random, time
import statistics

def quickSort(arr, low, high, m, contador):
    if low < high:
        contador["comparacoes"] += 1
        if high - low > m:
            contador["comparacoes"] += 1
            pi = partition(arr, low, high, contador)
            quickSort(arr, low, pi - 1, m, contador)
            quickSort(arr, pi + 1, high, m, contador)
        else:
            insertionSort(arr, low, high, contador)

def partition(arr, low, high, contador):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        contador["comparacoes"] += 1
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j, contador)

    swap(arr, i + 1, high, contador)
    return i + 1

def insertionSort(arr, low, high, contador):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            contador["comparacoes"] += 1
            arr[j + 1] = arr[j]
            contador["trocas"] += 1
            j -= 1
        contador["comparacoes"] += 1
        arr[j + 1] = key

def swap(arr, i, j, contador):
    contador["trocas"] += 1
    arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    n = 1000
    arr_base = [random.randint(0, 1000) for _ in range(n)]
    repeticoes = 30  # número de vezes que cada M será testado

    resultados = []

    for m in range(1, 100):  # testando M de 1 até 100
        tempos = []
        comparacoes = []
        trocas = []
        for _ in range(repeticoes):
            arr = arr_base[:]  # cópia do vetor
            contador = {"comparacoes": 0, "trocas": 0}
            start = time.time()
            quickSort(arr, 0, n - 1, m, contador)
            end = time.time()
            tempos.append(end - start)
            comparacoes.append(contador["comparacoes"])
            trocas.append(contador["trocas"])

        resultados.append({
            "m": m,
            "tempo_medio": statistics.mean(tempos),
            "tempo_dp": statistics.stdev(tempos),
            "comparacoes_medias": statistics.mean(comparacoes),
            "trocas_medias": statistics.mean(trocas)
        })

    # Ordena pelo menor tempo médio
    resultados.sort(key=lambda x: x["tempo_medio"])

    # Exibe os 5 melhores valores de M
    for r in resultados[:5]:
        print(f"M = {r['m']}")
        print(f"Tempo médio: {r['tempo_medio']:.6f} s (± {r['tempo_dp']:.6f})")
        print(f"Comparações médias: {r['comparacoes_medias']:.2f}")
        print(f"Trocas médias: {r['trocas_medias']:.2f}")
        print()

import time
import statistics
import matplotlib.pyplot as plt
import pandas as pd

def quickSort(arr, low, high, m, contador):
    if low < high:
        if high - low > m:
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
    arquivo = "vetor_repetidos.txt"

    with open(arquivo, "r") as f:
        arr_base = [int(x) for x in f.read().split()]

    n = len(arr_base)
    repeticoes = 30
    resultados = []

    for m in range(1, 100):
        tempos = []
        comparacoes = []
        trocas = []
        for _ in range(repeticoes):
            arr = arr_base[:]
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
            "comparacoes_medias": statistics.mean(comparacoes),
            "trocas_medias": statistics.mean(trocas)
        })

    # Ordenar resultados por tempo médio
    resultados.sort(key=lambda x: x["tempo_medio"])

    # Criar DataFrame para tabela
    df = pd.DataFrame(resultados)
    print("\nMelhor resultado: ", arquivo)
    for r in resultados[:1]:
        print(f"M = {r['m']}")
        print(f"Tempo médio: {r['tempo_medio']:.6f} s")
        print(f"Comparações médias: {r['comparacoes_medias']:.2f}")
        print(f"Trocas médias: {r['trocas_medias']:.2f}")
        print()

    # Reordenar resultados por m para os gráficos (para linhas contínuas)
    resultados.sort(key=lambda x: x["m"])

    ms = [r['m'] for r in resultados]
    tempos = [r['tempo_medio'] for r in resultados]
    comparacoes = [r['comparacoes_medias'] for r in resultados]
    trocas = [r['trocas_medias'] for r in resultados]

    # Gráfico combinado
    plt.figure(figsize=(12, 8))
    plt.plot(ms, tempos, marker='o', label='Tempo Médio (s)')
    plt.plot(ms, [c / max(comparacoes) * max(tempos) for c in comparacoes], marker='x', label='Comparações (normalizado)')
    plt.plot(ms, [t / max(trocas) * max(tempos) for t in trocas], marker='^', label='Trocas (normalizado)')
    plt.xlabel('Valor de m')
    plt.ylabel('Valores (normalizados para comparação)')
    plt.title('Comparação Normalizada: Tempo, Comparações e Trocas vs m')
    plt.grid(True)
    plt.legend()
    plt.savefig('combinado_vs_m.png')
    plt.close()

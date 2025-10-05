import time
import statistics
import matplotlib.pyplot as plt
import pandas as pd

def quickSort(arr, low, high, m, contador):
    contador["comparacoes"] += 1
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
        contador["comparacoes"] += 1  # cada comparação arr[j] < pivot
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j, contador)
    swap(arr, i + 1, high, contador)
    return i + 1

def insertionSort(arr, low, high, contador):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low:
            contador["comparacoes"] += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                contador["trocas"] += 1
                j -= 1
            else:
                break
        arr[j + 1] = key

def swap(arr, i, j, contador):
    if i != j:
        contador["trocas"] += 1
        arr[i], arr[j] = arr[j], arr[i]

def executar_quicksort(arquivo, m):
    with open(arquivo, "r") as f:
        arr_base = [int(x) for x in f.read().split()]

    arr = arr_base[:]
    contador = {"comparacoes": 0, "trocas": 0}

    start = time.time()
    quickSort(arr, 0, len(arr) - 1, m, contador)
    end = time.time()

    return {
        "arquivo": arquivo,
        "tempo": end - start,
        "comparacoes": contador["comparacoes"],
        "trocas": contador["trocas"]
    }


if __name__ == "__main__":
    arquivos = {
        "Ordenado": "vetor_ordenado.txt",
        "Aleatório": "vetor_aleatorio.txt",
        "Inverso": "vetor_inverso.txt",
        "Repetidos": "vetor_repetidos.txt"
    }

    resultados = []

    m = 25

    for nome, arquivo in arquivos.items():
        resultado = executar_quicksort(arquivo, m)
        resultado["tipo"] = nome
        resultados.append(resultado)

    for resultado in resultados:
        print(resultado["trocas"])

    # Organizar resultados em DataFrame
    df = pd.DataFrame(resultados, columns=["tipo", "tempo", "comparacoes", "trocas"])

    # Plotando gráfico simples
    df.plot(x="tipo", y=["tempo", "comparacoes", "trocas"], kind="bar", subplots=True, figsize=(10, 8))
    plt.tight_layout()
    plt.show()
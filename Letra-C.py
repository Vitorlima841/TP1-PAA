import random, time

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
    numeros_ordenados = sorted([arr[high], arr[low], arr[(low + high) // 2]])
    pivot = numeros_ordenados[1]
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
    arr = [random.randint(0, 1000) for _ in range(n)]

    resultados = []

    for m in range(1, 10000):
        copia = arr[:]
        contador = {"comparacoes": 0, "trocas": 0}
        start = time.time()
        quickSort(copia, 0, n - 1, m, contador)
        end = time.time()

        tempo = round(end - start, 6)
        resultados.append({
            "m": m,
            "tempo": tempo,
            "comparacoes": contador["comparacoes"],
            "trocas": contador["trocas"]
        })

    resultados.sort(key=lambda x: x["tempo"])

    for r in resultados[:3]:
        print(f"M = {r['m']}")
        print("Tempo:", r["tempo"], "s")
        print("Comparações:", r["comparacoes"])
        print("Trocas:", r["trocas"])
        print()

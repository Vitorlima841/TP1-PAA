def partition(arr, low, high):

    numeros_ordenados = sorted(arr[high], arr[low], arr[high/2])
    pivot = numeros_ordenados[1]
    
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    
    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr, low, high, m):
    if low < high:
        
        if(high - low > m):
            pi = partition(arr, low, high)
        else:
            insertionSort(arr)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    m = 100
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)

    quickSort(arr, 0, n - 1, m)
    
    for val in arr:
        print(val, end=" ")


print()

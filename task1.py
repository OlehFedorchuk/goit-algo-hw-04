import timeit
import random
import pandas as pd

# Реалізація сортування злиттям (Merge Sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Реалізація сортування вставками (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Функція для бенчмаркування алгоритмів
def benchmark_sorting_algorithms():
    sizes = [100, 1000, 5000]
    results = []

    for size in sizes:
        data = [random.randint(0, 10000) for _ in range(size)]

        ms_time = timeit.timeit(lambda: merge_sort(data.copy()), number=3)
        is_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=3)
        ts_time = timeit.timeit(lambda: sorted(data.copy()), number=3)

        results.append({
            "Size": size,
            "Merge Sort (s)": ms_time,
            "Insertion Sort (s)": is_time,
            "Timsort (Python built-in) (s)": ts_time
        })

    return pd.DataFrame(results)

# Запуск і вивід результатів
df = benchmark_sorting_algorithms()
print(df)
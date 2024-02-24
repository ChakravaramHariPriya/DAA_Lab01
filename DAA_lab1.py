import random
import time

def generate_random_array(size=100, min_value=1, max_value=100):
    return [random.randint(min_value, max_value) for _ in range(size)]

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def measure_sort_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

def main():
    array_size = 1000
    random_array = generate_random_array(size=array_size, min_value=1, max_value=1000)
    
    for sort_func in [selection_sort, bubble_sort, insertion_sort]:
        arr_copy = random_array.copy()
        time_taken = measure_sort_time(sort_func, arr_copy)
        print(f"{sort_func.__name__} took {time_taken:.6f} seconds to sort an array of size {array_size}.")

if __name__ == "__main__":
    main()

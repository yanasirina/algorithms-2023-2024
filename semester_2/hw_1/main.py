import time
import random
from algorithms import quick_sort, selection_sort, bubble_sort


array_sizes = [10, 100, 1000]
algorithms = [quick_sort, selection_sort, bubble_sort]


for array_size in array_sizes:
    array = [random.randint(0, 10_000) for _ in range(array_size)]
    for algorithm in algorithms:
        start_time = time.time()
        sorted_array = algorithm(array)
        total_time = time.time() - start_time
        # умножим время на 10000, чтобы избавить от лишних нулей (для простоты восприятия)
        display_time = total_time * 10000
        print(f'{algorithm.__name__} for size {array_size} is {display_time:4f}')
    print()

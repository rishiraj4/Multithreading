import threading
import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lesser = quicksort([x for x in arr[1:] if x < pivot])
    greater = quicksort([x for x in arr[1:] if x >= pivot])
    return lesser + [pivot] + greater

def threaded_quicksort(arr, depth=0, max_depth=2):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left_part = [x for x in arr[1:] if x < pivot]
    right_part = [x for x in arr[1:] if x >= pivot]

    left_sorted = []
    right_sorted = []

    if depth < max_depth:
        left_thread = threading.Thread(target=lambda: left_sorted.extend(threaded_quicksort(left_part, depth + 1, max_depth)))
        right_thread = threading.Thread(target=lambda: right_sorted.extend(threaded_quicksort(right_part, depth + 1, max_depth)))
        left_thread.start()
        right_thread.start()
        left_thread.join()
        right_thread.join()
    else:
        left_sorted = quicksort(left_part)
        right_sorted = quicksort(right_part)

    return left_sorted + [pivot] + right_sorted

if __name__ == "__main__":
    arr = [random.randint(0, 100000) for _ in range(100000)]

    print("Single-threaded Quicksort...")
    start = time.time()
    sorted_single = quicksort(arr.copy())
    print(f"Time: {time.time() - start:.4f} seconds")

    print("\nMulti-threaded Quicksort...")
    start = time.time()
    sorted_multi = threaded_quicksort(arr.copy())
    print(f"Time: {time.time() - start:.4f} seconds")

    print(f"\nResults match: {sorted_single == sorted_multi}")

import threading
import time
import random

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

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def threaded_merge_sort(arr, depth=0, max_depth=2):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    if depth >= max_depth:
        # Fallback to regular merge sort
        left = threaded_merge_sort(arr[:mid], depth+1, max_depth)
        right = threaded_merge_sort(arr[mid:], depth+1, max_depth)
    else:
        left = []
        right = []

        def sort_left():
            nonlocal left
            left = threaded_merge_sort(arr[:mid], depth+1, max_depth)

        def sort_right():
            nonlocal right
            right = threaded_merge_sort(arr[mid:], depth+1, max_depth)

        t1 = threading.Thread(target=sort_left)
        t2 = threading.Thread(target=sort_right)

        t1.start()
        t2.start()
        t1.join()
        t2.join()

    return merge(left, right)

if __name__ == "__main__":
    arr = [random.randint(0, 100000) for _ in range(100000)]

    print("Starting single-threaded sort...")
    start = time.time()
    sorted_arr = merge_sort(arr.copy())
    print(f"Single-threaded time: {time.time() - start:.4f} seconds")

    print("\nStarting multi-threaded sort...")
    start = time.time()
    threaded_sorted = threaded_merge_sort(arr.copy())
    print(f"Multi-threaded time: {time.time() - start:.4f} seconds")

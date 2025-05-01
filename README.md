Multithreaded Python Programming – Concurrency Assignment
This document contains solutions for three tasks that demonstrate the use of multithreading in Python to improve performance for sorting algorithms and file downloads.

Objective:
To implement multithreaded versions of common algorithms and compare their performance with traditional single-threaded versions.

Directory Structure:
├── merge_sort_multithreaded.py
├── quicksort_multithreaded.py
├── concurrent_downloader.py
├── README.md

Task 1: Multi-threaded Merge Sort

Description:
Implements a merge sort that uses the threading module to sort sub-arrays concurrently.

Approach:
- The array is split into two halves.
- Each half is sorted using a separate thread recursively.
- The final result is merged from sorted halves.
- Time comparison is shown between single-threaded and multi-threaded implementations.

How to Run:
python merge_sort_multithreaded.py

Task 2: Multi-threaded Quicksort

Description:
Implements a quicksort that uses threads to sort sub-arrays concurrently, with a controlled thread depth.

Approach:
- A pivot is chosen and the array is split into lesser and greater sublists.
- If the recursion depth is within the threshold (max_depth), new threads are used to sort the sublists.
- Otherwise, it falls back to normal quicksort.
- The result is a time comparison between both versions.

How to Run:
python quicksort_multithreaded.py

Task 3: Concurrent File Downloader

Description:
Downloads multiple files in parallel using threads and compares the performance with sequential downloading.

Approach:
- Accepts a list of URLs.
- Downloads files sequentially and records time taken.
- Downloads files concurrently using threading.Thread and compares speedup.

Default URLs used:
- https://www.example.com
- https://www.wikipedia.org
- https://www.python.org
- https://httpbin.org/html

You can modify the urls list in the script or read from a .txt file.

How to Run:
python concurrent_downloader.py
Ensure you have an internet connection and the requests library installed:

pip install requests

Sample Output
Each script prints the time taken by the single-threaded and multi-threaded (or concurrent) versions. This helps visualize performance benefits of using multithreading.

Author
Rishi Raj

Course: Advanced Programming

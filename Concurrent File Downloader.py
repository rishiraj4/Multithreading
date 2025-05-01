import threading
import requests
import time

def download_file(url, index):
    try:
        response = requests.get(url)
        with open(f"file_{index}.html", "wb") as f:
            f.write(response.content)
        print(f"Downloaded file_{index}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def sequential_download(urls):
    for i, url in enumerate(urls):
        download_file(url, i)

def concurrent_download(urls):
    threads = []
    for i, url in enumerate(urls):
        t = threading.Thread(target=download_file, args=(url, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    urls = [
        "https://www.example.com",
        "https://www.wikipedia.org",
        "https://www.python.org",
        "https://httpbin.org/html"
    ]

    print("Sequential download...")
    start = time.time()
    sequential_download(urls)
    print(f"Sequential time: {time.time() - start:.4f} seconds\n")

    print("Concurrent download...")
    start = time.time()
    concurrent_download(urls)
    print(f"Concurrent time: {time.time() - start:.4f} seconds")

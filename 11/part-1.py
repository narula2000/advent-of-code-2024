from functools import lru_cache
from concurrent.futures import ThreadPoolExecutor

data = "3028 78 973951 5146801 5 0 23533 857".split()


@lru_cache(None)
def split_string_in_half(s):
    # Calculate the midpoint
    mid = len(s) // 2

    # Split the string into two halves
    first_half = s[:mid]
    second_half = s[mid:]

    return first_half, second_half


@lru_cache(None)
def multiply_by_2024(n):
    return str(int(n) * 2024)


def process_chunk(chunk):
    # Process a chunk of data
    i = 0
    bound = len(chunk)
    while i < bound:
        curr = chunk[i]
        if curr == "0":
            chunk[i] = "1"
        elif len(curr) % 2 == 0:  # is even
            left, right = split_string_in_half(curr)
            right = str(int(right))
            chunk[i] = left
            chunk.insert(i + 1, right)
            bound = len(chunk)
            i += 1
        else:
            chunk[i] = multiply_by_2024(curr)
        i += 1
    return chunk


for blink in range(25):
    print("Blink", blink)

    # Divide data into chunks for parallel processing
    num_chunks = 4  # Number of parallel workers
    chunk_size = (len(data) + num_chunks - 1) // num_chunks
    chunks = [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]

    # Process chunks in parallel
    with ThreadPoolExecutor(max_workers=num_chunks) as executor:
        results = list(executor.map(process_chunk, chunks))

    # Combine processed chunks back into a single list
    data = [item for chunk in results for item in chunk]

print(len(data))

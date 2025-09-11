#Part 2 Answer:          6381624803796
#Part 2 time:            145819365 μs
#Part 2 memory:          2,156,779 bytes

import time

for i in range(1000001):
    percent = (i / 1000000) * 100
    print(f"\r{percent:.2f}% done", end='', flush=True)
    time.sleep(0.00001)  # Optional: slow down for visibility

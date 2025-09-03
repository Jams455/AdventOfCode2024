import time
import tracemalloc

def start_part_1(day_num):
    print("\n*************************************")
    print(f"*************** DAY {day_num} ***************")
    print("*************************************")

    tracemalloc.start()
    p1_start = time.perf_counter()

    return p1_start

def start_part_2():
    tracemalloc.start()
    p2_start = time.perf_counter()

    return p2_start

def end_part(part_answer, part_start, part_num):
    part_stop = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"\nPart {part_num} Answer:\t\t{part_answer}")
    print(f"Part {part_num} time:\t\t{round((part_stop - part_start)*1e6)} μs")
    print(f"Part {part_num} memory:\t\t{peak:,} bytes\n")


import time
import tracemalloc
import numpy as np

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

def get_input_file_str(day_num: int, test: bool):
    return f"Inputs/day_{day_num:02}_input{'_test' if test else ''}.txt"

def Is_In_Limits(arr: np.ndarray, coords: tuple) -> bool:
    if len(coords) != arr.ndim:
        return False
    return all(0 <= c < s for c, s in zip(coords, arr.shape))

def test_print(*args, testing=True, **kwargs):
    if testing:
        print(*args, **kwargs)

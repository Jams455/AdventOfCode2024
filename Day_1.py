import numpy as np
from formatting_fns import *
from collections import Counter

left_list, right_list = np.loadtxt("Day_1_Input_Test.txt", delimiter=None, unpack=True, dtype=np.int64)

##########################
part1_start = start_part_1(1)
######### PART 1 #########

left_list.sort()
right_list.sort()

assert len(left_list) == len(right_list)

distances = np.abs(left_list - right_list)

part1_answer = distances.sum()

##########################
end_part(part1_answer, part1_start, 1)
part2_start = start_part_2()
######### PART 2 #########

left_counts = Counter(left_list)
right_counts = Counter(right_list)

part2_answer = sum(
    val * left_counts[val] * right_counts[val]
    for val in left_counts
    if val in right_counts
)

##########################
end_part(part2_answer, part2_start, 2)
##########################

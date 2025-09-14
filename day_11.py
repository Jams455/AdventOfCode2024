from utils.helper import *
import numpy as np
from collections import defaultdict

DAY_NUM = 11
TEST = False

# import file
np_stones = np.loadtxt(get_input_file_str(DAY_NUM, TEST), dtype=int, delimiter=' ')

##########################
part1_start = start_part_1(DAY_NUM)
######### PART 1 #########

part1_answer = 0

# part 1 code

def calc_child_stones(curr_stone):
    if curr_stone == 0:
        return [1]
    elif len(str(curr_stone)) % 2 == 0:
        s_stone = str(curr_stone)
        r_stone = int(s_stone[int(len(s_stone)/2):])
        l_stone = int(s_stone[0:int(len(s_stone)/2)])

        return [l_stone, r_stone]
    else:
        return [curr_stone * 2024]

def gen_memory_graph(curr_stones, target):
    stones_graph = defaultdict(list)

    for i in range(target):
        next_stones = []

        for curr_stone in curr_stones:
            child_stones = stones_graph[curr_stone]
            if child_stones == []:
                child_stones = calc_child_stones(curr_stone)
                stones_graph[curr_stone] = child_stones
                next_stones += child_stones

        curr_stones = next_stones

    print()

    return stones_graph

def visit_stone(stones_graph, curr_stone, curr_depth, target):
    total_children = 0

    if curr_depth == target:
        return 1
    
    for child in stones_graph[curr_stone]:
        next_depth = curr_depth + 1
        total_children += visit_stone(stones_graph, child, next_depth, target)

    return total_children

TARGET = 25

curr_stones = np_stones.tolist()

stones_graph = gen_memory_graph(curr_stones, TARGET)

for stone in np_stones.tolist():
    part1_answer += visit_stone(stones_graph, stone, 0, TARGET)

##########################
end_part(part1_answer, part1_start, 1)
part2_start = start_part_2()
######### PART 2 #########

part2_answer = 0
 
# part 2 code

def visit_stone_with_mem(stones_graph, curr_stone, curr_depth, target):
    total_children = 0

    if curr_depth == target:
        return 1
    
    key = (curr_stone, curr_depth)
    mem_value = mem[key]

    if mem_value != 0:
        return mem_value
    
    for child in stones_graph[curr_stone]:
        next_depth = curr_depth + 1
        total_children += visit_stone_with_mem(stones_graph, child, next_depth, target)

    mem[key] = total_children

    return total_children

TARGET = 75

mem = defaultdict(int)

curr_stones = np_stones.tolist()

stones_graph = gen_memory_graph(curr_stones, TARGET)

for stone in np_stones.tolist():
    part2_answer += visit_stone_with_mem(stones_graph, stone, 0, TARGET)

##########################
end_part(part2_answer, part2_start, 2)
##########################

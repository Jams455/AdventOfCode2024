import numpy as np
from utils.helper import *
from collections import defaultdict

DAY_NUM = 5
TEST = False

with open(get_input_file_str(DAY_NUM, TEST)) as f:
    lines = [line.strip() for line in f]

all_pages = set()
after_map = defaultdict(list)
updates = []

for line in lines:
    if '|' in line:
        before, after = [int(x) for x in line.split('|')]

        all_pages.update([before, after])
        after_map[before].append(after)

    elif ',' in line:
        update_sequence = np.array([page_num for page_num in line.split(',')], dtype=int)
        updates.append(update_sequence)

##########################
part1_start = start_part_1(5)
######### PART 1 #########

part1_answer = 0

incorrectly_ordered_updates = []

for update in updates:
    is_correctly_ordered = True
    for i in range(1, len(update)):
        previous_nodes_in_update = set(update[0:i])
        nodes_that_must_come_after = set(after_map[update[i]])

        if previous_nodes_in_update & nodes_that_must_come_after:
            is_correctly_ordered = False
            break
    if is_correctly_ordered:
        part1_answer += update[int((len(update) - 1) / 2)]
    else:
        incorrectly_ordered_updates.append(update)

##########################
end_part(part1_answer, part1_start, 1)
part2_start = start_part_2()
######### PART 2 #########

def dfs(node, incorrect_update):
    if node in visiting:
        print("LOOP ERROR")
        exit()
        ...

    visiting.add(node)

    for next_node in (set(after_map[node]) & set(incorrect_update)):
        if next_node not in visited:
            dfs(next_node, incorrect_update)
            
    visited.add(node)
    visiting.remove(node)
    topo_order.append(node)

part2_answer = 0

for incorrect_update in incorrectly_ordered_updates:
    visited = set()
    visiting = set()
    topo_order = []

    for node in incorrect_update:
        if node not in visited:
            dfs(node, incorrect_update)
            visited.add(node)

    corrected_order = [int(x) for x in topo_order[::-1]]
    part2_answer += corrected_order[int((len(corrected_order) - 1) / 2)]

##########################
end_part(part2_answer, part2_start, 2)
##########################

import numpy as np
from collections import defaultdict

with open("Day_5/Day_5_Input.txt") as f:
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

for key, value in after_map.items():
    #print(f"{key}\t:\t{value}")
    ...

######### PART 1 #########

incorrectly_ordered_updates = []
total = 0

for update in updates:
    is_correctly_ordered = True
    for i in range(1, len(update)):
        previous_nodes_in_update = set(update[0:i])
        nodes_that_must_come_after = set(after_map[update[i]])

        if previous_nodes_in_update & nodes_that_must_come_after:
            is_correctly_ordered = False
            break
    if is_correctly_ordered:
        total += update[int((len(update) - 1) / 2)]
    else:
        incorrectly_ordered_updates.append(update)

print(f"Part 1 Answer:\t{total}")

######### PART 2 #########

def dfs(node, incorrect_update):
    if node in visiting:
        print("LOOP ERROR")
        exit()
        ...

    visiting.add(node)

    for next_node in (set(after_map[node]) & set(incorrect_update)):
        if next_node not in visited:
            visit_stack.append(next_node)
            dfs(next_node, incorrect_update)
            
    visited.add(node)
    visiting.remove(node)
    topo_order.append(node)

corrected_total = 0

for incorrect_update in incorrectly_ordered_updates:
    visited = set()
    visiting = set()
    visit_stack = []
    topo_order = []

    for node in incorrect_update:
        if node not in visited:
            visit_stack.append(node)

            dfs(node, incorrect_update)

            visited.add(node)

    corrected_order = [int(x) for x in topo_order[::-1]]
    corrected_total += corrected_order[int((len(corrected_order) - 1) / 2)]

print(f"Part 2 Answer:\t{corrected_total}")

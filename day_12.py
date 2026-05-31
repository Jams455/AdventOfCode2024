from utils.helper import *
import numpy as np

DAY_NUM = 12
TEST = False

# import file
with open(get_input_file_str(DAY_NUM, TEST)) as f:
    data = np.array([np.array([*line.strip()]) for line in f])

##########################
part1_start = start_part_1(DAY_NUM)
######### PART 1 #########

part1_answer = 0

# part 1 code

TRANSLATIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))

visited = np.zeros_like(data)

def visit(plant, i, j):
    if not Is_In_Limits(data, (i, j)) or data[i][j] != plant:
        return (0, 1) # ( area addition, perimiter addition )
    
    elif visited[i][j]:
        return (0, 0)
    
    else:
        visited[i][j] = 1
        area_addition = 1
        perim_addition = 0

        for Δi, Δj in TRANSLATIONS:
            next_area_addition, next_perim_addition = visit(plant, i+Δi, j+Δj)
            area_addition += next_area_addition
            perim_addition += next_perim_addition
        
        return (area_addition, perim_addition)

for i, row in enumerate(data):
    for j, val in enumerate(row):
        curr_plant = data[i][j]
        area, perim = visit(curr_plant, i, j)

        part1_answer += area * perim

##########################
end_part(part1_answer, part1_start, 1)
part2_start = start_part_2()
######### PART 2 #########

part2_answer = 0

# part 2 code

visited = np.zeros_like(data)

FLAG = 0
borders = [[], [], [], []]

def visit(plant, i, j):
    if not Is_In_Limits(data, (i, j)) or data[i][j] != plant:
        global FLAG
        FLAG = 1

        return (0, 1) # ( area addition, perimiter addition )
    
    elif visited[i][j]:
        return (0, 0)
    
    else:
        visited[i][j] = 1
        area_addition = 1
        perim_addition = 0

        for t, (Δi, Δj) in enumerate(TRANSLATIONS):
            next_area_addition, next_perim_addition = visit(plant, i+Δi, j+Δj)
            area_addition += next_area_addition
            perim_addition += next_perim_addition
            
            if FLAG:
                borders[t].append((i, j))
                FLAG = 0
        
        return (area_addition, perim_addition)

def strip(arr, coords, t):
    if coords in arr:
        arr.remove(coords)

        new_coords = (coords[0] + TRANSLATIONS[t][0], coords[1] + TRANSLATIONS[t][1])

        strip(arr, new_coords, t)

def border_count(borders):
    edges = []
    for t in range(4):
        while len(borders[t]) > 0:
            start = borders[t][0]

            strip(borders[t], start, (t+1)%4)

            below = (start[0] - TRANSLATIONS[(t+1)%4][0], start[1] - TRANSLATIONS[(t+1)%4][1])
            strip(borders[t], below, (t-1)%4)

            edges.append(start)
    
    return len(edges)

for i, row in enumerate(data):
    for j, val in enumerate(row):
        curr_plant = data[i][j]
        area, perim = visit(curr_plant, i, j)

        border_cnt = border_count(borders)
        
        borders = [[], [], [], []]
        
        part2_answer += area * border_cnt

##########################
end_part(part2_answer, part2_start, 2)
##########################

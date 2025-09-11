from utils.helper import *
import numpy as np

DAY_NUM = 10
TEST = False

# import file
with open(get_input_file_str(DAY_NUM, TEST)) as f:
    data = np.array([np.array([*line.strip()]) for line in f])

##########################
part1_start = start_part_1(DAY_NUM)
######### PART 1 #########

part1_answer = 0

# part 1 code

translations = ((-1, 0), (0, 1), (1, 0), (0, -1))

visited_ends = []

def dfs(data, coords, curr_height, unique_destination):
    if curr_height == 9 and coords not in visited_ends:
        if unique_destination:
            visited_ends.append(coords)
        return 1

    total = 0

    for translation in translations:
        next_coords = ( coords[0] + translation[0],
                        coords[1] + translation[1] )
        
        next_goal_height = curr_height + 1

        if Is_In_Limits(data, next_coords):
            next_height = int(data[next_coords])

            if next_height == next_goal_height:
                total += dfs(data, next_coords, next_goal_height, unique_destination)

    return total

for row_ind, row in enumerate(data):
    for col_ind, height in enumerate(row):
        if height == '0':
            part1_answer += dfs(data, (row_ind, col_ind), 0, unique_destination=True)

            visited_ends.clear()

##########################
end_part(part1_answer, part1_start, 1)
part2_start = start_part_2()
######### PART 2 #########

part2_answer = 0

# part 2 code

visited_ends.clear()

for row_ind, row in enumerate(data):
    for col_ind, height in enumerate(row):
        if height == '0':
            part2_answer += dfs(data, (row_ind, col_ind), 0, unique_destination=False)

##########################
end_part(part2_answer, part2_start, 2)
##########################

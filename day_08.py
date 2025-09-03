from utils.helper import *
from collections import defaultdict
import numpy as np

DAY_NUM = 8
TEST = False

# import file and extract data

data = []
antenna_coords_dict = defaultdict(list)

with open(get_input_file_str(DAY_NUM, TEST)) as f:
    for line_num, line in enumerate(f):
        formatted_line = np.array([*line.strip()])

        for col_num, char in enumerate(line):
            if char != '.' and char != '\n':
                antenna_coords_dict[char].append((line_num, col_num))

        data.append(formatted_line)
    
    data = np.array(data)

antinode_map_1 = np.full_like(data, '.')

##########################
part1_start = start_part_1(DAY_NUM)
######### PART 1 #########

part1_answer = 0

for antenna_freq_symb in antenna_coords_dict.keys():
    for base_coords in antenna_coords_dict[antenna_freq_symb]:
        for target_coords in antenna_coords_dict[antenna_freq_symb]:
            if base_coords == target_coords:
                continue
            
            antinode_coords_row = 2 * target_coords[0] - base_coords[0]
            antinode_coords_col = 2 * target_coords[1] - base_coords[1]

            antinode_coords_tuple = (antinode_coords_row, antinode_coords_col)

            if Is_In_Limits(antinode_map_1, antinode_coords_tuple):
                if antinode_map_1[antinode_coords_row][antinode_coords_col] == '.':
                    part1_answer += 1

                antinode_map_1[antinode_coords_row][antinode_coords_col] = '#'

for row in antinode_map_1:
    test_print(row, testing=TEST)

##########################
end_part(part1_answer, part1_start, 1)
part2_start = start_part_2()
######### PART 2 #########

part2_answer = 0

antinode_map_2 = np.full_like(antinode_map_1, '.')

for antenna_freq_symb in antenna_coords_dict.keys():
    for base_coords in antenna_coords_dict[antenna_freq_symb]:
        for target_coords in antenna_coords_dict[antenna_freq_symb]:
            if base_coords == target_coords:
                continue
                    
            antinode_dir_vec = (target_coords[0] - base_coords[0], target_coords[1] - base_coords[1])
            dir_vec_multiplyer = 0

            while True:
                dir_vec_multiplyer += 1
                antinode_coords_tuple = (base_coords[0] + dir_vec_multiplyer * antinode_dir_vec[0],
                                            base_coords[1] + dir_vec_multiplyer * antinode_dir_vec[1])

                if not Is_In_Limits(antinode_map_2, antinode_coords_tuple):
                    break

                if antinode_map_2[antinode_coords_tuple] == '.':
                    part2_answer += 1

                antinode_map_2[antinode_coords_tuple] = '#'

for row in antinode_map_2:
    test_print(row, testing=TEST)

##########################
end_part(part2_answer, part2_start, 2)
##########################

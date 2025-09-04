from utils.helper import *
import numpy as np

DAY_NUM = 9
TEST = False

# import file
with open(get_input_file_str(DAY_NUM, TEST)) as f:
    disk_map = np.array([*f.read().strip()], dtype=np.int8)

##########################
part1_start = start_part_1(DAY_NUM)
######### PART 1 #########

def calc_checksum(inp) -> int:
    file_checksum = 0
    for i, char in enumerate(inp):
        file_checksum += i * int(char)
    return file_checksum

part1_answer = 0

final_message = []

back_pointer = disk_map.size - 1
back_file_id = (disk_map.size - 1) / 2

assert round(back_file_id) == back_file_id
back_file_id = int(back_file_id)

for front_pointer in range(disk_map.size):
    front_file_id = round(front_pointer / 2)

    if front_pointer % 2 == 0:
        final_message += [front_file_id] * int(disk_map[front_pointer])
        disk_map[front_pointer] = 0
    else:
        while disk_map[front_pointer]:
            if disk_map[back_pointer] == 0:
                disk_map[back_pointer - 1] = 0
                back_pointer -= 2
                back_file_id -= 1
                continue
            
            disk_map[front_pointer] -= 1
            disk_map[back_pointer] -= 1
            final_message.append(back_file_id)

part1_answer = calc_checksum(final_message)

##########################
end_part(part1_answer, part1_start, 1)
part2_start = start_part_2()
######### PART 2 #########

part2_answer = 0

# part 2 code

##########################
end_part(part2_answer, part2_start, 2)
##########################

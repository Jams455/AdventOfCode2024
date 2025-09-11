from utils.helper import *
import numpy as np

DAY_NUM = 9
TEST = False

# import file
with open(get_input_file_str(DAY_NUM, TEST)) as f:
    disk_map = np.array([*f.read().strip()], dtype=np.int8)

disk_map_static = disk_map.copy()

##########################
part1_start = start_part_1(DAY_NUM)
######### PART 1 #########

def calc_checksum(inp) -> int:
    file_checksum = 0
    for i, char in enumerate(inp):
        if char == '.':
            continue
        file_checksum += i * int(char)
    return file_checksum

part1_answer = 0

# part 1 code

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
disk_map = disk_map_static.copy()

# part 2 code

final_message = []

front_pointer = 0

for front_pointer in range(disk_map.size):
    back_pointer = disk_map.size - 1

    percent_done = front_pointer / back_pointer * 100
    print(f"\r{percent_done:.2f}% done", end='', flush=True)

    front_file_id = round(front_pointer / 2)
    back_file_id = (disk_map.size - 1) / 2
    assert round(back_file_id) == back_file_id
    back_file_id = int(back_file_id)

    if front_pointer % 2 == 0:
        if disk_map[front_pointer] != 10:
            final_message += [front_file_id] * int(disk_map[front_pointer])
        else:
            final_message += ['.'] * int(disk_map_static[front_pointer])
    else:
        b_found = True
        while b_found:
            space = disk_map[front_pointer]

            while disk_map[back_pointer] > space:
                back_pointer -= 2
                back_file_id -= 1

                if back_pointer < front_pointer:
                    b_found = False
                    break

            if b_found:
                final_message += [back_file_id] * int(disk_map[back_pointer])
                disk_map[front_pointer] -= int(disk_map[back_pointer])
                disk_map[back_pointer] = 10

                space = disk_map[front_pointer]
        
        final_message += ['.'] * space

part2_answer = calc_checksum(final_message)

##########################
end_part(part2_answer, part2_start, 2)
##########################

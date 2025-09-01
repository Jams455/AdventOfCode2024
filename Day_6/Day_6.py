import numpy as np

with open("Day_6/Day_6_Input_Test.txt") as f:
    data = np.array([np.array([*line.strip()]) for line in f])

######### PART 1 #########

def b_In_Limits(nd_array, pos):
    limits = np.shape(nd_array)

    return 0 <= pos[0] < limits[0] and 0 <= pos[1] < limits[1]

total = 0

limits = np.shape(data)

direction_from_state = (np.array([-1, 0]), np.array([0, 1]), np.array([1, 0]), np.array([0, -1]))
symbol_from_state = ('^', '>', 'v', '<')
bin_marker_from_state = (0b1000, 0b0100, 0b0010, 0b0001)
state = 0

coords = np.array([x[0] for x in np.where(data == '^')])
next_coords = coords + direction_from_state[state]

while 0 <= next_coords[0] < limits[0] and 0 <= next_coords[1] < limits[1]:
    current_symbol = data[tuple(coords)]
    next_symbol = data[tuple(next_coords)]

    if next_symbol == '.':
        if current_symbol == '.' or current_symbol == '^':
            data[tuple(coords)] = 'x'
            total += 1
        coords = next_coords
        next_coords = coords + direction_from_state[state]
    elif next_symbol == 'x':
        if current_symbol == '.':
            data[tuple(coords)] = 'x'
            total += 1
        coords = next_coords
        next_coords = coords + direction_from_state[state]
    elif next_symbol == '#':
        state = ( state + 1 ) % 4
        next_coords = coords + direction_from_state[state]

data[tuple(coords)] = 'x'
total += 1

print(f"Part 1 Answer:\t{total}")

######### PART 2 #########

upper_limits = np.shape(data)
lower_limits = (0, 0)

dir_from_state = (np.array([-1, 0]), np.array([0, 1]), np.array([1, 0]), np.array([0, -1]))
mkr_from_state = (0b1000, 0b0100, 0b0010, 0b0001)
smb_from_state = ('^', '>', 'v', '<')

history_bitmap = np.zeros_like(data, dtype=np.int8)

coords = np.array([x[0] for x in np.where(data == '^')])
state = 0

while True:
    if history_bitmap[tuple(coords)] & mkr_from_state[state]:
        print("Loop Detected")
        break 
    else:
        history_bitmap[tuple(coords)] |= mkr_from_state[state]

        next_coords = coords + dir_from_state[state]

        if 0 <= next_coords[0] < upper_limits[0] and 0 <= next_coords[1] < upper_limits[1]

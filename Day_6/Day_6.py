import numpy as np

with open("Day_6/Day_6_Input.txt") as f:
    data = np.array([np.array([*line.strip()]) for line in f])

def Is_In_Limits(nd_array, pos):
    limits = np.shape(nd_array)

    return 0 <= pos[0] < limits[0] and 0 <= pos[1] < limits[1]

######### PART 1 #########

visited_positions = []

state = 0

dir_from_state = (np.array([-1, 0]), np.array([0, 1]), np.array([1, 0]), np.array([0, -1]))

coords = np.array([x[0] for x in np.where(data == '^')])
ini_coords = tuple(coords)
next_coords = coords + dir_from_state[state]

total = 0

while Is_In_Limits(data, next_coords):
    current_symbol = data[tuple(coords)]
    next_symbol = data[tuple(next_coords)]

    if next_symbol == '.' or next_symbol == 'x':
        if current_symbol == '.' or current_symbol == '^':
            data[tuple(coords)] = 'x'
            total += 1
            visited_positions.append(tuple(coords))
        coords = next_coords
        next_coords = coords + dir_from_state[state]
    elif next_symbol == '#':
        state = ( state + 1 ) % 4
        next_coords = coords + dir_from_state[state]

data[tuple(coords)] = 'x'
total += 1
visited_positions.append(tuple(coords))

print(f"Part 1 Answer:\t{total}")

######### PART 2 #########

mkr_from_state = (0b1000, 0b0100, 0b0010, 0b0001)
num_of_loops = 0

i_max, j_max = data.shape

for i, j in visited_positions:
    if data[i, j] == '#':
        continue

    coords = np.array(ini_coords)
    state = 0

    history_bitmap = np.zeros_like(data, dtype=np.int8)

    data[i, j] = '#'

    while True:
        if history_bitmap[tuple(coords)] & mkr_from_state[state]:
            num_of_loops += 1
            break 
        else:
            history_bitmap[tuple(coords)] |= mkr_from_state[state]

            next_coords = coords + dir_from_state[state]

            if Is_In_Limits(history_bitmap, next_coords):
                if data[tuple(next_coords)] == '#':
                    state = (state + 1) % 4
                    continue
                else:
                    coords = next_coords
                    continue
            else:
                break

    data[i, j] = '.'
    
print(f"Part 2 Answer:\t{num_of_loops}")

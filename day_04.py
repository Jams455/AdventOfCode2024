from utils.helper import *
import numpy as np

DAY_NUM = 4
TEST = False

rows = np.loadtxt(get_input_file_str(DAY_NUM, TEST), unpack=True, delimiter=None, dtype=str)

##########################
part1_start = start_part_1(4)
######### PART 1 #########

part1_answer = 0

for i in range(rows.size):
    for j in range(len(rows[i])):
        if rows[i][j] != 'X':
            continue

        #north
        if i >= 3:
            if (rows[i][j] + rows[i-1][j] + rows[i-2][j] + rows[i-3][j]) == "XMAS":
                part1_answer += 1

        #east
        if j <= len(rows[i]) - 4:
            if (rows[i][j] + rows[i][j+1] + rows[i][j+2] + rows[i][j+3]) == "XMAS":
                part1_answer += 1

        #south
        if i <= len(rows) - 4:
            if (rows[i][j] + rows[i+1][j] + rows[i+2][j] + rows[i+3][j]) == "XMAS":
                part1_answer += 1

        #west
        if j >= 3:
            if (rows[i][j] + rows[i][j-1] + rows[i][j-2] + rows[i][j-3]) == "XMAS":
                part1_answer += 1

        #north-east
        if i >= 3 and j <= len(rows[i]) - 4:
            if (rows[i][j] + rows[i-1][j+1] + rows[i-2][j+2] + rows[i-3][j+3]) == "XMAS":
                part1_answer += 1

        #north-west
        if i >= 3 and j >= 3:
            if (rows[i][j] + rows[i-1][j-1] + rows[i-2][j-2] + rows[i-3][j-3]) == "XMAS":
                part1_answer += 1

        #south-east
        if i <= len(rows) - 4 and j <= len(rows[i]) - 4:
            if (rows[i][j] + rows[i+1][j+1] + rows[i+2][j+2] + rows[i+3][j+3]) == "XMAS":
                part1_answer += 1

        #south-west
        if i <= len(rows) - 4 and j >= 3:
            if (rows[i][j] + rows[i+1][j-1] + rows[i+2][j-2] + rows[i+3][j-3]) == "XMAS":
                part1_answer += 1

##########################
end_part(part1_answer, part1_start, 1)
part2_start = start_part_2()
######### PART 2 #########

part2_answer = 0

for i in range(1, rows.size - 1):
    for j in range(1, len(rows[i]) - 1):
        if rows[i][j] != 'A':
            continue
        
        if  ((rows[i-1][j-1] == 'M' and rows[i+1][j+1] == 'S') or (rows[i-1][j-1] == 'S' and rows[i+1][j+1] == 'M')) \
        and ((rows[i-1][j+1] == 'M' and rows[i+1][j-1] == 'S') or (rows[i-1][j+1] == 'S' and rows[i+1][j-1] == 'M')):
            part2_answer += 1

##########################
end_part(part2_answer, part2_start, 2)
##########################

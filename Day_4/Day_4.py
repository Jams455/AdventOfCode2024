import numpy as np

rows = np.loadtxt("Day_4/Day_4_Input.txt", unpack=True, delimiter=None, dtype=str)

######### PART 1 #########

xmas_counts = 0

for i in range(rows.size):
    for j in range(len(rows[i])):
        if rows[i][j] != 'X':
            continue

        #north
        if i >= 3:
            if (rows[i][j] + rows[i-1][j] + rows[i-2][j] + rows[i-3][j]) == "XMAS":
                xmas_counts += 1

        #east
        if j <= len(rows[i]) - 4:
            if (rows[i][j] + rows[i][j+1] + rows[i][j+2] + rows[i][j+3]) == "XMAS":
                xmas_counts += 1

        #south
        if i <= len(rows) - 4:
            if (rows[i][j] + rows[i+1][j] + rows[i+2][j] + rows[i+3][j]) == "XMAS":
                xmas_counts += 1

        #west
        if j >= 3:
            if (rows[i][j] + rows[i][j-1] + rows[i][j-2] + rows[i][j-3]) == "XMAS":
                xmas_counts += 1

        #north-east
        if i >= 3 and j <= len(rows[i]) - 4:
            if (rows[i][j] + rows[i-1][j+1] + rows[i-2][j+2] + rows[i-3][j+3]) == "XMAS":
                xmas_counts += 1

        #north-west
        if i >= 3 and j >= 3:
            if (rows[i][j] + rows[i-1][j-1] + rows[i-2][j-2] + rows[i-3][j-3]) == "XMAS":
                xmas_counts += 1

        #south-east
        if i <= len(rows) - 4 and j <= len(rows[i]) - 4:
            if (rows[i][j] + rows[i+1][j+1] + rows[i+2][j+2] + rows[i+3][j+3]) == "XMAS":
                xmas_counts += 1

        #south-west
        if i <= len(rows) - 4 and j >= 3:
            if (rows[i][j] + rows[i+1][j-1] + rows[i+2][j-2] + rows[i+3][j-3]) == "XMAS":
                xmas_counts += 1

print(f"XMAS Counts:\t{xmas_counts}")

######### PART 2 #########

x_mas_counts = 0

for i in range(1, rows.size - 1):
    for j in range(1, len(rows[i]) - 1):
        if rows[i][j] != 'A':
            continue
        
        if  ((rows[i-1][j-1] == 'M' and rows[i+1][j+1] == 'S') or (rows[i-1][j-1] == 'S' and rows[i+1][j+1] == 'M')) \
        and ((rows[i-1][j+1] == 'M' and rows[i+1][j-1] == 'S') or (rows[i-1][j+1] == 'S' and rows[i+1][j-1] == 'M')):
            x_mas_counts += 1

print(f"X-MAS Counts:\t{x_mas_counts}")

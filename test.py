TRANSLATIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))

border_arr = [[(0, 0), (0, 1), (0, 2), (1, 5), (0, 3)], [(0, 3)], [(0, 3), (0, 2), (0, 1), (0, 0)], [(0, 0)]]



def strip(arr, coords, t):
    if coords in arr:
        arr.remove(coords)

        new_coords = (coords[0] + TRANSLATIONS[t][0], coords[1] + TRANSLATIONS[t][1])

        strip(arr, new_coords, t)

def border_count(borders):
    edges = []
    for t in range(3):
        start = borders[t][0]

        while len(borders[t]) > 0:
            start = borders[t][0]

            strip(borders[t], start, (t+1)%4)

            below = (start[0] - TRANSLATIONS[(t+1)%4][0], start[1] - TRANSLATIONS[(t+1)%4][1])
            strip(borders[t], below, (t-1)%4)

            edges.append(start)
    
    return len(edges)

borders = border_count(border_arr)

print(borders)

for i in range(3):
    print(i)

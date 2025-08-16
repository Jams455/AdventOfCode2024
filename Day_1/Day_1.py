import numpy as np

left_list, right_list = np.loadtxt("Day_1/Day_1_Input.txt", delimiter=None, unpack=True, dtype=np.int64)

left_list.sort()
right_list.sort()

######### PART 1 #########

distances = np.abs(left_list - right_list)

total_distance = distances.sum()

print(f"Total Distance:\t\t{total_distance}")

######### PART 2 #########

similarity_score = 0

for left_num in left_list:
    for right_num in right_list:
        if left_num == right_num:
            similarity_score += left_num

print(f"Similarity Score:\t{similarity_score}")

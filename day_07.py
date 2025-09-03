from utils.helper import *
import numpy as np

DAY_NUM = 7
TEST = False

targets = []
numbers = []

with open(get_input_file_str(DAY_NUM, TEST)) as i_f:
    for i_line in i_f:
        i_target, i_number_list = i_line.split(':')
        targets.append(int(i_target))
        i_number_list = i_number_list.strip().split(' ')
        numbers.append(np.array(i_number_list, dtype=np.int_))

##########################
part1_start = start_part_1(DAY_NUM)
######### PART 1 #########

def Compute_Equation(number_list, operator_list: str, target):
    total = number_list[0]

    for k, char in enumerate(operator_list):
        if char == '0':
            total *= number_list[k+1]
        elif char == '1':
            total += number_list[k+1]
        elif char == '2':
            total = int(str(total) + str(number_list[k+1]))
        
        if total > target:
            return total

    return total

part1_answer = 0

for i in range(len(targets)):
    lim = 2 ** (len(numbers[i])-1)

    for j in range(lim):
        operators_str = bin(j)[2:].rjust(len(numbers[i]) - 1, '0')

        total = Compute_Equation(numbers[i], operators_str, targets[i])

        if total == targets[i]:
            part1_answer += targets[i]
            break

##########################
end_part(part1_answer, part1_start, 1)
part2_start = start_part_2()
######### PART 2 #########

part2_answer = 0

for i in range(len(targets)):
    lim = 3 ** (len(numbers[i])-1)
    
    for j in range(lim):
        operators_str = np.base_repr(j, 3).rjust(len(numbers[i]) - 1, '0')

        total = Compute_Equation(numbers[i], operators_str, targets[i])

        if total == targets[i]:
            part2_answer += targets[i]
            break

##########################
end_part(part2_answer, part2_start, 2)
##########################

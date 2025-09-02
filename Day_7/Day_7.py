import numpy as np

TEST = False

def test_print(*args, **kwargs):
    if TEST:
        print(*args, **kwargs)

targets = []
numbers = []

with open(["Day_7/Day_7_Input.txt", "Day_7/Day_7_Input_Test.txt"][TEST]) as i_f:
    for i_line in i_f:
        i_target, i_number_list = i_line.split(':')
        targets.append(int(i_target))
        i_number_list = i_number_list.strip().split(' ')
        numbers.append(np.array(i_number_list, dtype=np.int_))

######### PART 1 #########


def Compute_Equation(number_list, operator_list: str):
    test_print(number_list[0], end='')
    total = number_list[0]

    for k, char in enumerate(operator_list):
        if int(char) == 0:
            test_print('+', end='')
            total *= number_list[k+1]
        elif int(char) == 1:
            test_print('*', end='')
            total += number_list[k+1]
        elif int(char) == 2:
            test_print('|', end='')
            total = int(str(total) + str(number_list[k+1]))

        test_print(number_list[k+1], end='')
    
    test_print('\t\t', total, '\t\t', end='')

    return total


total_of_matches = 0

for i in range(len(targets)):
    test_print('\n\n\t', targets[i], '\n', numbers[i])

    lim = 2 ** (len(numbers[i])-1)

    for j in range(lim):
        operators_str = bin(j)[2:].rjust(len(numbers[i]) - 1, '0')

        total = Compute_Equation(numbers[i], operators_str)

        if total == targets[i]:
            test_print("Match!")
            total_of_matches += targets[i]
            break
        else:
            test_print("No Match")

print(f"Part 1 Answer:\t{total_of_matches}")

######### PART 2 #########

total_of_matches = 0

for i in range(len(targets)):
    test_print('\n\n\t', targets[i], '\n', numbers[i])

    lim = 3 ** (len(numbers[i])-1)
    
    for j in range(lim):
        operators_str = np.base_repr(j, 3).rjust(len(numbers[i]) - 1, '0')

        total = Compute_Equation(numbers[i], operators_str)

        if total == targets[i]:
            test_print("Match!")
            total_of_matches += targets[i]
            break
        else:
            test_print("No Match")

print(f"Part 2 Answer:\t{total_of_matches}")

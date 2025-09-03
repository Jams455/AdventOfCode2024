from utils.helper import *
import numpy as np
import re
import parse

DAY_NUM = 3
TEST = False

with open(get_input_file_str(DAY_NUM, TEST)) as f:
    text = f.read()

##########################
part1_start = start_part_1(3)
######### PART 1 #########

part1_answer = 0

results = re.findall(r"mul\([0-9]*,[0-9]*\)", text)

format = parse.compile("mul({},{})")
for result in results:
    numbers = np.array(format.parse(result)[:], dtype=np.int32)
    part1_answer += numbers[0] * numbers[1]

##########################
end_part(part1_answer, part1_start, 1)
part2_start = start_part_2()
######### PART 2 #########

part2_answer = 0

results = re.findall(r"do\(\)|don't\(\)|mul\([0-9]*,[0-9]*\)", text)

currently_multiplying = True
format = parse.compile("mul({},{})")
for result in results:
    if result == "don't()":
       currently_multiplying = False
    elif result == "do()":
       currently_multiplying = True
    elif currently_multiplying:
        numbers = np.array(format.parse(result)[:], dtype=np.int32)
        part2_answer += numbers[0] * numbers[1]

##########################
end_part(part2_answer, part2_start, 2)
##########################

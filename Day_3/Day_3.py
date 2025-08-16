import numpy as np
import re
import parse
 
text = ""
with open("Day_3/Day_3_Input.txt") as f:
  for x in f:
    text += x

######### PART 1 #########

results = re.findall(r"mul\([0-9]*,[0-9]*\)", text)

total = 0
format = parse.compile("mul({},{})")
for result in results:
    numbers = np.array(format.parse(result)[:], dtype=np.int32)
    total += numbers[0] * numbers[1]

print(f"Part 1 Answer:\t{total}")

######### PART 2 #########

results = re.findall(r"do\(\)|don't\(\)|mul\([0-9]*,[0-9]*\)", text)

total = 0
currently_multiplying = True
format = parse.compile("mul({},{})")
for result in results:
    if result == "don't()":
       currently_multiplying = False
    elif result == "do()":
       currently_multiplying = True
    elif currently_multiplying:
        numbers = np.array(format.parse(result)[:], dtype=np.int32)
        total += numbers[0] * numbers[1]

print(f"Part 2 Answer:\t{total}")

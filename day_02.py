from utils.helper import *
import numpy as np

DAY_NUM = 2
TEST = False

reports = []
with open(get_input_file_str(DAY_NUM, TEST)) as f:
  for x in f:
    reports.append(np.array(x.split(), dtype=np.int64))

##########################
part1_start = start_part_1(2)
######### PART 1 #########

def Validate_Report(report):
    differences = report[1:] - report[0:-1]
    if (differences.max() <= 3 and differences.min() >= 1) or (differences.max() <= -1 and differences.min() >= -3):
        return True
    return False

part1_answer = 0

for report in reports:
    if Validate_Report(report):
        part1_answer += 1

##########################
end_part(part1_answer, part1_start, 1)
part2_start = start_part_2()
######### PART 2 #########

part2_answer = 0
for report in reports:
    if Validate_Report(report):
        part2_answer += 1
    else:
        for i in range(report.size):
            new_report = np.delete(report, i)
            if Validate_Report(new_report):
                part2_answer += 1
                break

##########################
end_part(part2_answer, part2_start, 2)
##########################

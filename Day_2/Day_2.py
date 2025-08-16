import numpy as np

reports = []
with open("Day_2/Day_2_Input.txt") as f:
  for x in f:
    reports.append(np.array(x.split(), dtype=np.int64))

######### PART 1 #########


def Validate_Report(report):
    differences = report[1:] - report[0:-1]
    if (differences.max() <= 3 and differences.min() >= 1) or (differences.max() <= -1 and differences.min() >= -3):
        return True
    return False


num_of_safe_reports = 0

for report in reports:
    if Validate_Report(report):
        num_of_safe_reports += 1

print(f"Number of safe reports without deletes:\t{num_of_safe_reports}")

######### PART 2 #########

num_of_safe_reports = 0

for report in reports:
    if Validate_Report(report):
        num_of_safe_reports += 1
    else:
        for i in range(report.size):
            new_report = np.delete(report, i)
            if Validate_Report(new_report):
                num_of_safe_reports += 1
                break

print(f"Number of safe reports with deletes:\t{num_of_safe_reports}")

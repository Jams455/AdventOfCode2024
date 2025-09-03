import os

TEMPLATE_PATH = os.path.join("utils", "day_template.py")
PROBLEMS_DIR = "Problems"
INPUTS_DIR = "Inputs"

def get_next_day_number(existing_files):
    day_numbers = []

    for f in existing_files:
        if f.startswith("day_") and f.endswith(".py"):
            try:
                num = int(f[4:6])  # Extract two-digit number
                day_numbers.append(num)
            except ValueError:
                continue

    next_day = max(day_numbers, default=0) + 1
    return f"{next_day:02}"  # Zero-padded (01, 02, ...)

def create_day_files(day_num):
    # Paths
    py_filename = f"day_{day_num}.py"
    problem_path = os.path.join(PROBLEMS_DIR, f"Day_{day_num}.txt")
    input_path = os.path.join(INPUTS_DIR, f"Day_{day_num}_Input.txt")
    test_input_path = os.path.join(INPUTS_DIR, f"Day_{day_num}_Input_Test.txt")

    # Create directories
    os.makedirs(PROBLEMS_DIR, exist_ok=True)
    os.makedirs(INPUTS_DIR, exist_ok=True)

    # Create .py file from template
    if not os.path.exists(py_filename):
        if os.path.exists(TEMPLATE_PATH):
            with open(TEMPLATE_PATH, "r") as template_file:
                contents = template_file.readlines()

            # Replace DAY_NUM line
            for i, line in enumerate(contents):
                if "DAY_NUM = " in line:
                    contents[i] = f"DAY_NUM = {int(day_num)}\n"
                    break

            with open(py_filename, "w") as new_file:
                new_file.writelines(contents)
        else:
            print(f"[!] Template file not found at {TEMPLATE_PATH}")
            return

    # Create input files
    for path in [problem_path, input_path, test_input_path]:
        if not os.path.exists(path):
            open(path, "w").close()

    print(f"[✓] Created files for Day {day_num}.")

if __name__ == "__main__":
    files_in_root = os.listdir()
    next_day = get_next_day_number(files_in_root)
    create_day_files(next_day)

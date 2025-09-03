import os
import re
from pathlib import Path
import shutil

BASE_DIR = Path(__file__).parent.resolve()
TEMPLATE_PATH = BASE_DIR / "Template.py"
DAYS_DIR = BASE_DIR  # All Day_XX folders live here

def find_existing_days():
    day_folders = [d for d in os.listdir(DAYS_DIR) if re.match(r"^Day_\d{2}$", d)]
    day_numbers = [int(re.search(r"\d{2}", name).group()) for name in day_folders]
    return sorted(day_numbers)

def create_day_folder(day_num: int):
    day_str = f"{day_num:02d}"  # Zero-padded (e.g. 09)
    day_name = f"Day_{day_str}"
    folder_path = DAYS_DIR / day_name

    try:
        folder_path.mkdir()
        print(f"[+] Created folder: {day_name}")
    except FileExistsError:
        print(f"[!] Folder already exists: {day_name}")
        return

    # File paths inside the new folder
    py_file = folder_path / f"{day_name}.py"
    desc_file = folder_path / f"{day_name}.txt"
    input_file = folder_path / f"{day_name}_Input.txt"
    test_input_file = folder_path / f"{day_name}_Input_Test.txt"

    # Create Python file from Template.py with replacements
    if not TEMPLATE_PATH.exists():
        print(f"[!] ERROR: Template.py not found in root directory.")
        return

    with open(TEMPLATE_PATH, "r") as f:
        template_code = f.read()

    # Replace placeholders
    template_code = template_code.replace("Day_X", day_name).replace("X", str(int(day_str)))

    with open(py_file, "w") as f:
        f.write(template_code)

    # Create empty text files
    for fpath in [desc_file, input_file, test_input_file]:
        fpath.touch()

    print(f"[+] Created files in {day_name}:")
    print(f"    - {py_file.name} (from Template.py)")
    print(f"    - {desc_file.name}")
    print(f"    - {input_file.name}")
    print(f"    - {test_input_file.name}")

def create_next_day():
    existing_days = find_existing_days()
    next_day = (max(existing_days) + 1) if existing_days else 1
    create_day_folder(next_day)

if __name__ == "__main__":
    create_next_day()

import os
import shutil
import re

# Config
ROOT = os.path.dirname(__file__)
DAY_PATTERN = re.compile(r'Day[_\- ]?(\d{1,2})', re.IGNORECASE)

# Get all files in the current directory
all_files = [f for f in os.listdir(ROOT) if os.path.isfile(os.path.join(ROOT, f))]

# Process each file
for filename in all_files:
    match = DAY_PATTERN.match(filename)
    if match:
        day_num = int(match.group(1))
        folder_name = f"Day_{str(day_num).zfill(2)}"
        folder_path = os.path.join(ROOT, folder_name)

        # Create folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        # Move the file
        src_path = os.path.join(ROOT, filename)
        dst_path = os.path.join(folder_path, filename)
        shutil.move(src_path, dst_path)
        print(f"Moved {filename} -> {folder_name}/")

print("\n✅ Done! All day files organized into folders.")

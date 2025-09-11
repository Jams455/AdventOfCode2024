import glob
import importlib.util
import os


for file in sorted(glob.glob("day_*.py")):
    print(f"Running {file}...")
    exec(open(file).read())

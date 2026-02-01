import os

from constans import path_dir

path = os.path.join(path_dir, "06_01_file_handling_lab", "my_first_file.txt")

if os.path.exists(path):
    os.remove(path)
else:
    print("File already deleted")
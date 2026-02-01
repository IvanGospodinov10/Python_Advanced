import os
import re

from constans import path_dir

path = os.path.join(path_dir, 'files')

with open(os.path.join(path, "word.txt")) as file:
    words = file.read().split()

with open(os.path.join(path, "input.txt")) as file:
    text = file.read()

data = {}
for word in words:
    pattern = rf"\b{word}\b"
    matches = re.findall(pattern, text, re.IGNORECASE)
    data[word] = len(matches)

ordered_data = sorted(data.items(), key=lambda x: -x[1])

with open(os.path.join(path, "output.txt"), "w") as file:
    for word, count in ordered_data:
        file.write(f"{word}: {count}\n")

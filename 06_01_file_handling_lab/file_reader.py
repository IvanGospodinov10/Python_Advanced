import os

from constans import path_dir

path = os.path.join(path_dir, 'files', 'numbers.txt')

file = open(path)

numbers = [int(el) for el in file.read().split("\n") if el]
print(sum(numbers))

# total = 0

# for line in file:
#     total += int(line)

# print(total)
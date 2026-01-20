rows, cols = [int(el) for el in input().split()]

matrix = []

starting_character = ord("a")

for row in range(rows):
    line = []
    for col in range(cols):
        line.append(chr(starting_character) + chr(starting_character + col) + chr(starting_character))
    matrix.append(line)
    starting_character += 1

for row in range(rows):
    print(*matrix[row])

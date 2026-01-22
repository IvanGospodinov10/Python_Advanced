n = int(input())

matrix = []
allice = []
tea_bags = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "A":
            allice = [row, col]
            matrix[row][col] = "*"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while tea_bags < 10:
    direction = input()
    move = directions[direction]
    new_row = allice[0] + move[0]
    new_col = allice[1] + move[1]
    if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
        break

    if matrix[new_row][new_col] == "R":
        matrix[new_row][new_col] = "*"
        break

    if matrix[new_row][new_col] not in ".*":
        tea_bags += int(matrix[new_row][new_col])

    matrix[new_row][new_col] = "*"
    allice = [new_row, new_col]

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*row) for row in matrix]

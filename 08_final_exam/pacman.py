n = int(input())
health = 100
immunity = False

matrix = []

total_stars = 0
cur_row = cur_col = None

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "P":
            cur_row, cur_col = row, col
        if matrix[row][col] == "*":
            total_stars += 1

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


def handle_outside_matrix_move(r, c):
    if r < 0:
        r = n - 1
    elif r >= n:
        r = 0
    if c < 0:
        c = n - 1
    elif c >= n:
        c = 0

    return r, c


matrix[cur_row][cur_col] = "-"

while health > 0:
    command = input()

    if command == "end":
        break

    move = direction[command]
    new_row = cur_row + move[0]
    new_col = cur_col + move[1]

    if not (0 <= new_row < n and 0 <= new_col < n):
        new_row, new_col = handle_outside_matrix_move(new_row, new_col)

    cell = matrix[new_row][new_col]

    if cell == "-":
        cur_row, cur_col = new_row, new_col
    elif cell == "*":
        cur_row, cur_col = new_row, new_col
        total_stars -= 1
        matrix[new_row][new_col] = "-"
        if total_stars == 0:
            break
    elif cell == "F":
        immunity = True
        cur_row, cur_col = new_row, new_col
        matrix[new_row][new_col] = "-"
    elif cell == "G":
        if immunity:
            immunity = False
            matrix[new_row][new_col] = "-"
            cur_row, cur_col = new_row, new_col

        else:
            health -= 50

            matrix[new_row][new_col] = "-"
            cur_row, cur_col = new_row, new_col
            if health <= 0:
                break

matrix[cur_row][cur_col] = "P"

if health <= 0:
    print(f"Game over! Pacman last coordinates [{cur_row},{cur_col}]")
elif total_stars == 0:
    print("Pacman wins! All the stars are collected.")
else:
    print("Pacman failed to collect all the stars.")

print(f"Health: {health}")
if total_stars > 0:
    print(f"Uncollected stars: {total_stars}")
for row in matrix:
    print(*row, sep='')

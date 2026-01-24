presents = int(input())
n = int(input())

matrix = []
santa_p = []
nice_kids = 0
total_presents = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "S":
            santa_p = [row, col]
        if matrix[row][col] == "V":
            nice_kids += 1

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while presents > 0:
    command = input()

    if command == "Christmas morning":
        break
    move = directions[command]
    row = santa_p[0] + move[0]
    col = santa_p[1] + move[1]

    if row < 0 or row >= n or col < 0 or col >= n:
        continue

    matrix[santa_p[0]][santa_p[1]] = "-"
    # santa_p = [row, col]

    if matrix[row][col] == "V":
        total_presents += 1
        presents -= 1
        # matrix[row][col] = "-"
    elif matrix[row][col] == "C":
        for d_row, d_col in directions.values():
            n_row, n_col = row + d_row, col + d_col

            if matrix[n_row][n_col] in ("V", "X"):
                if presents == 0:
                    break
                if matrix[n_row][n_col] == "V":
                    total_presents += 1
                presents -= 1
                matrix[n_row][n_col] = "-"
    santa_p = [row, col]
    matrix[santa_p[0]][santa_p[1]] = "S"

    if presents == 0:
        break

if presents == 0 and nice_kids - total_presents > 0:
    print("Santa ran out of presents!")

for row in matrix:
    print(" ".join(row))

if nice_kids - total_presents == 0:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - total_presents} nice kid/s.")

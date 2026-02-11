n, m = [int(x) for x in input().split(", ")]

matrix = []

curr_row = curr_col = None
bomb_row = bomb_col = None

for row in range(n):
    matrix.append(list(input()))
    for col in range(m):
        if matrix[row][col] == "C":
            curr_row, curr_col = row, col
        if matrix[row][col] == "B":
            bomb_row, bomb_col = row, col

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

start_row, start_col = curr_row, curr_col
round_time = 16
needed_time = 0

while True:
    command = input()

    if command == "defuse":
        if curr_row == bomb_row and curr_col == bomb_col:
            # Correct position
            if round_time >= 4:
                round_time -= 4
                matrix[curr_row][curr_col] = "D"
                print("Counter-terrorist wins!")
                print(f"Bomb has been defused: {round_time} second/s remaining.")
                break
            else:
                needed_time = 4 - round_time
                matrix[curr_row][curr_col] = "X"
                print("Terrorists win!")
                print("Bomb was not defused successfully!")
                print(f"Time needed: {needed_time} second/s.")
                break
        else:

            round_time -= 2
            if round_time <= 0:
                print("Terrorists win!")
                print("Bomb was not defused successfully!")
                print("Time needed: 0 second/s.")
                break
            continue

    if command in direction:

        round_time -= 1
        if round_time <= 0:
            print("Terrorists win!")
            print("Bomb was not defused successfully!")
            print("Time needed: 0 second/s.")
            break

        dr, dc = direction[command]
        new_r, new_c = curr_row + dr, curr_col + dc

        # Out of bounds
        if not (0 <= new_r < n and 0 <= new_c < m):
            continue

        cell = matrix[new_r][new_c]

        if cell == "T":
            matrix[new_r][new_c] = "*"
            print("Terrorists win!")
            break

        if cell == "B":
            curr_row, curr_col = new_r, new_c
            continue

        if cell == "*":
            curr_row, curr_col = new_r, new_c
            continue

matrix[start_row][start_col] = "C"

for row in matrix:
    print("".join(row))

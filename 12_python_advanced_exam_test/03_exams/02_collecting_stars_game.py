n = int(input())

field = []

p_row = p_col = None
collected_stars = 2

for row in range(n):
    field.append(input().split())
    for col in range(n):
        if field[row][col] == "P":
            p_row, p_col = row, col

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


def handle_outside_field(matrix, p_row, p_col, collected_stars):
    cell = matrix[0][0]

    if cell == "#":
        collected_stars -= 1
        return p_row, p_col, collected_stars, True
    elif cell == "*":

        collected_stars += 1
        field[0][0] = "."
        return 0, 0, collected_stars, False

    else:
        return 0, 0, collected_stars, False


field[p_row][p_col] = "."

while True:
    command = input()

    move = direction[command]
    new_row = p_row + move[0]
    new_col = p_col + move[1]

    if not (0 <= new_row < n and 0 <= new_col < n):
        p_row, p_col, collected_stars, should_continue = handle_outside_field(field, p_row, p_col, collected_stars)

        if collected_stars == 0:
            print(f"Game over! You are out of any stars.")
            print(f"Your final position is [{p_row}, {p_col}]")
            break

        if collected_stars == 10:
            print("You won! You have collected 10 stars.")
            print(f"Your final position is [{p_row}, {p_col}]")
            break

        if should_continue:
            continue

    else:
        cell = field[new_row][new_col]

        if cell == "#":
            collected_stars -= 1
            if collected_stars == 0:
                print(f"Game over! You are out of any stars.")
                print(f"Your final position is [{p_row}, {p_col}]")
                break
            continue
        elif cell == "*":
            p_row, p_col = new_row, new_col
            collected_stars += 1
            field[p_row][p_col] = "."
            if collected_stars == 10:
                print(f"You won! You have collected 10 stars.")
                print(f"Your final position is [{p_row}, {p_col}]")
                break
        else:
            p_row, p_col = new_row, new_col

field[p_row][p_col] = "P"
for row in field:
    print(*row, sep=" ")

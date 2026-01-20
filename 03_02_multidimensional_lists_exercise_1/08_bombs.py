n  = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(n)]
bombs = input().split()

directions = {
    (0, -1), (0, 1), (1, 0), (-1, 0),
    (-1, -1), (1, -1), (-1, 1), (1, 1)
}

for bomb in bombs:
    row, col = [int(el) for el in bomb.split(",")]
    explosion = matrix[row][col]

    if explosion <= 0:
        continue

    matrix[row][col] = 0

    for row_direction, col_direction in directions:
        new_row, new_col = row + row_direction, col + col_direction
        if 0 <= new_row < n and 0 <= new_col < n and matrix[new_row][new_col] > 0:
            matrix[new_row][new_col] -= explosion


# alive_cells = 0
# for row in matrix:
#     for x in row:
#         if x > 0:
#             alive_cells += 1
alive_cells = sum(1 for row in matrix for x in row if x > 0)
sum_of_cells = sum(x for row in matrix for x in row if x > 0)

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_cells}")

for row in matrix:
    print(*row)
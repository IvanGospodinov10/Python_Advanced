rows, cols = [int(x) for x in input().split()]

matrix = [[char for char in input().split()] for _ in range(rows)]

counter_match = 0

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_character = matrix[row_index][col_index]
        left_character = matrix[row_index][col_index + 1]
        down_character = matrix[row_index + 1][col_index]
        diagonal_character = matrix[row_index + 1][col_index + 1]

        if (current_character == left_character and
                current_character == down_character and
                current_character == diagonal_character):
            counter_match += 1

print(counter_match)

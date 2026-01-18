n = int(input())

matrix = []
symbol_index = []

for _ in range(n):
    matrix.append(list(input()))

searched_symbol = input()

for row_index in range(n):
    for col_index in range(n):
        if searched_symbol == matrix[row_index][col_index]:
            print(f"({row_index}, {col_index})")
            exit()

print(f"{searched_symbol} does not occur in the matrix")

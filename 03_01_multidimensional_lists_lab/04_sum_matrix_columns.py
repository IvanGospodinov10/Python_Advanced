rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for row in range(rows):
    line = [int(el) for el in input().split(" ")]
    matrix.append(line)


for col in range(cols):
    columns_sum = 0
    for row in range(rows):
        columns_sum += matrix[row][col]
    print(columns_sum)
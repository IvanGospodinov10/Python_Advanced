rows, cols = list(map(int, input().split(", ")))

matrix = []

for row in range(rows):
    lines = [int(x) for x in input().split(", ")]
    matrix.append(lines)

total_sum = 0

for row in range(rows):
    total_sum += sum(matrix[row])
print(total_sum)
print(matrix)

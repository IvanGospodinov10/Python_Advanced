n = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

primary_diagonal = []
secondary_diagonal = []

for row_index in range(n):
    primary_diagonal.append(matrix[row_index][row_index])
    secondary_diagonal.append(matrix[row_index][-row_index - 1])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")

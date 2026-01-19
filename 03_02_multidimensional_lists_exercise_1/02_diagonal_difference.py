n = int(input())

matrix = [[int(x) for x in input().split(" ")] for _ in range(n)]

primary_diagonal = []
secondary_diagonal = []

for row in range(n):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][-row - 1])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
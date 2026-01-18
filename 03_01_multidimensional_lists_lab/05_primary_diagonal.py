n = int(input())

matrix = []
primary_diagonal = 0

for _ in range(n):
    matrix.append([int(el) for el in input().split()])

for row in range(n):
    primary_diagonal += matrix[row][row]
print(primary_diagonal)
n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command = input().split()

    if command[0] == 'END':
        break

    row, col, number = map(int, command[1:])
    if 0<= row < n and 0<= col < n:
        if command[0] == "Add":
            matrix[row][col] += number
        elif command[0] == "Subtract":
            matrix[row][col] -= number
    else:
        print("Invalid coordinates")

for row in matrix:
    print(*row)

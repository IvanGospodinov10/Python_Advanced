n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command = input().split()

    if command[0] == 'END':
        break

    index_1 = int(command[1])
    index_2 = int(command[2])
    number = int(command[3])


    if 0<= index_1 < n and 0<= index_2 < n:
        if command[0] == "Add":
            matrix[index_1][index_2] += number
        elif command[0] == "Subtract":
            matrix[index_1][index_2] -= number
    else:
        print("Invalid coordinates")

for row in matrix:
    print(*row)

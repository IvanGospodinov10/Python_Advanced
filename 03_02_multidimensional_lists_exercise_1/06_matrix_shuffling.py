rows, cols = [int(el) for el in input().split()]

matrix = [[x for x in input().split()] for _ in range(rows)]


while True:
    line = input().split()
    command = line[0]
    if command == "END":
        break
    if command != "swap" or len(line) != 5:
        print("Invalid input!")
        continue
    r1, c1, r2, c2 = [int(x) for x in line[1:]]
    if 0 <= r1 < rows and 0 <= c1 < cols and 0 <= r2 < rows and 0 <= c2 < cols:
        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
        for row in range(rows):
            print(*matrix[row])
    else:
        print("Invalid input!")
METEOR_DAMAGE = 5
REFUEL = 10
MOVE = 5

n = int(input())
energy = 100
mission_success = False

matrix = []
space_ship = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "S":
            space_ship = [row, col]

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while energy >= MOVE:
    command = input()
    move = direction[command]

    new_row = space_ship[0] + move[0]
    new_col = space_ship[1] + move[1]

    if not (0 <= new_row < n and 0 <= new_col < n):
        print("Mission failed! The spaceship was lost in space.")
        break

    if matrix[space_ship[0]][space_ship[1]] != "R":
        matrix[space_ship[0]][space_ship[1]] = "."

    energy -= MOVE
    cell = matrix[new_row][new_col]

    if cell == "R":
        energy = min(100, energy + REFUEL)
        space_ship = [new_row, new_col]
        continue

    if cell == "M":
        energy -= METEOR_DAMAGE
        matrix[new_row][new_col] = "."

    if cell == "P":
        mission_success = True
        space_ship = [new_row, new_col]
        print(f"Mission accomplished! The spaceship reached Planet B with {energy} resources left.")
        break

    if energy < MOVE:
        space_ship = [new_row, new_col]
        print("Mission failed! The spaceship was stranded in space.")
        break

    space_ship = [new_row, new_col]

if not mission_success:
    matrix[space_ship[0]][space_ship[1]] = "S"

for row in matrix:
    print(" ".join(row))

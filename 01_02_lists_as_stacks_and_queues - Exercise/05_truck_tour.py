from collections import deque

petrol_pumps = int(input())
pumps = deque()

for _ in range(petrol_pumps):
    curr_fuel, curr_dist = input().split()
    pumps.append({"fuel": int(curr_fuel), "dist": int(curr_dist)})

start_position = 0
stops = 0

while stops < petrol_pumps:
    fuel = 0
    for i in range(petrol_pumps):
        fuel += pumps[i]["fuel"]
        dist = pumps[i]["dist"]
        if fuel <= dist:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        else:
            fuel -= dist
            stops += 1
print(start_position)

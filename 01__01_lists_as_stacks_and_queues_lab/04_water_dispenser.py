from collections import deque
water_qty = int(input())
people_queue = deque()
name = input()

while name != "Start":
    people_queue.append(name)
    name = input()

command = input()

while command != 'End':
    if 'refill'in command:
        command, litters = command.split(' ')
        water_qty += int(litters)
    else:
        drink = int(command)
        if drink <= water_qty:
            water_qty -= drink
            print(f"{people_queue.popleft()} got water")
        else:
            print(f"{people_queue.popleft()} must wait" )
    command = input()

print(f"{water_qty} liters left")
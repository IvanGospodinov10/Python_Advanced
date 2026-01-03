from collections import deque

green_light_duration = int(input())
free_window_pass = int(input())

cars = deque()
cars_passed = 0

while True:
    command = input()
    if command == "END":
        break
    if command != "green":
        cars.append(command)
        continue

    current_green_light = green_light_duration

    while cars and  current_green_light > 0:
        car = cars.popleft()
        if len(car) <= current_green_light:
            current_green_light -= len(car)
            cars_passed += 1
        else:
            remaining = len(car) - current_green_light

            if remaining <= free_window_pass:
                cars_passed += 1
            else:
                hit_index = current_green_light + free_window_pass
                print("A crash happened!")
                print(f"{car} was hit at {car[hit_index]}.")
                exit()
            current_green_light = 0

print("Everyone is safe.")
print(f"{cars_passed} total cars passed the crossroads.")

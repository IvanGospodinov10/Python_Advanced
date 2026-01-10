n = int(input())

cars = set()

for _ in range(n):
    direction, number = input().split(", ")

    if direction == "IN":
        cars.add(number)
    elif direction == "OUT":
        if number in cars:
            cars.remove(number)

if len(cars) == 0:
    print("Parking Lot is Empty")
else:
    for car in cars:
        print(car)

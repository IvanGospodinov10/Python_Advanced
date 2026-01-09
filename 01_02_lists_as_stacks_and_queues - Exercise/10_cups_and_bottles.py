from collections import deque

cups = deque(int(x) for x in input().split())
bottles = [int(x) for x in input().split()]

wasted_water = 0

while cups and bottles:
    cup = cups[0]
    bottle = bottles[-1]
    while cup > 0:
        if cup > bottle:
            cup = cup - bottle
            bottles.pop()
            bottle = bottles[-1]
        else:
            wasted_water += bottle - cup
            cup = cup - bottle
            bottles.pop()
            cups.popleft()

if cups and not bottles:
    print(f'Cups: {" ".join(map(str, cups))}')
    print(f"Wasted litters of water: {wasted_water}")
else:
    while bottles:
        print(f"Bottles: {bottles.pop()}", end=' ')
        print(f"\nWasted litters of water: {wasted_water}")
from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk_cups = deque(int(x) for x in input().split(", "))

milkshakes = 0

while chocolates and milk_cups and milkshakes < 5:
    if chocolates[-1] <= 0 and milk_cups[0] <= 0:
        milk_cups.popleft()
        chocolates.pop()
        continue
    else:
        if milk_cups[0] <= 0:
            milk_cups.popleft()
            continue
        if chocolates[-1] <= 0:
            chocolates.pop()
            continue
    if not chocolates or not milk_cups:
        break

    if chocolates[-1] == milk_cups[0]:
        milkshakes += 1
        chocolates.pop()
        milk_cups.popleft()
    else:
        chocolates[-1] -= 5
        milk_cups.rotate(-1)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join(str(x) for x in milk_cups)}")
else:
    print("Milk: empty")

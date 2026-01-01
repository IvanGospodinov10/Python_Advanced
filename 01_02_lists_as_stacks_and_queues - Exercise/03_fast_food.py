from collections import deque

food_qty = int(input())
orders = deque(int(x) for x in input().split())
orders_completed = []
max_order = max(orders)

while orders:

    if food_qty > 0:
        if food_qty > orders[0]:
            current_order = orders.popleft()
            food_qty -= current_order
            orders_completed.append(current_order)
        else:
            break
if orders:
    print(max_order)
    print(f"Orders left: ", *orders)
else:
    print(max_order)
    print(f"Orders complete")

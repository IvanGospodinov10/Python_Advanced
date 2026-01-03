from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(int(x) for x in input().split())
money = int(input())

shots = 0

while locks and bullets:
    shots += 1
    curr_bullet = bullets.pop()
    money -= bullet_price

    if curr_bullet <= locks[0]:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")
    if shots == gun_barrel_size and bullets:
        print("Reloading!")
        shots = 0

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${money}" )
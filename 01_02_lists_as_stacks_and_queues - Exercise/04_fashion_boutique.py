clothes = input().split()
rack_capacity = int(input())
racks = 0

while clothes:
    racks += 1
    current_rack_capacity = rack_capacity
    while clothes and int(clothes[-1]) <= current_rack_capacity:
        current_rack_capacity -= int(clothes.pop())

print(racks)

n, m = input().split()

set_n = set()
set_m = set()

for _ in range(int(n)):
    number = int(input())
    set_n.add(number)

for _ in range(int(m)):
    number = int(input())
    set_m.add(number)

result = set_n.intersection(set_m)

for num in result:
    print(num)
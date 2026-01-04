n = int(input())

names = set()

for _ in range(n):
    text = input()
    names.add(text)

for name in names:
    print(name)

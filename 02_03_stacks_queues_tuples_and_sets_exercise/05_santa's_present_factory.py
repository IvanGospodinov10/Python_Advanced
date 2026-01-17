from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

presents = {150: "Doll",
            250: "Wooden train",
            300: "Teddy bear",
            400: "Bicycle"
            }

crafted_toys = {}

while materials and magic:
    magic_level = materials[-1] * magic[0]

    if magic_level in presents:
        materials.pop()
        magic.popleft()
        new_toy = presents[magic_level]

        if new_toy not in crafted_toys:
            crafted_toys[new_toy] = 0
        crafted_toys[new_toy] += 1

    elif magic_level < 0:
        materials.append(materials.pop() + magic.popleft())

    elif magic_level > 0:
        magic.popleft()
        materials[-1] += 15

    else:
        if materials[-1] == 0:
            materials.pop()

        if magic[0] == 0:
            magic.popleft()

if (f"Doll" in crafted_toys and "Wooden train" in crafted_toys) or (f"Teddy bear" in crafted_toys and "Bicycle" in crafted_toys):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for key, value in sorted(crafted_toys.items()):
    print(f"{key}: {value}")



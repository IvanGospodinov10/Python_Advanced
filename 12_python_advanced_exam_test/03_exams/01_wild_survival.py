from collections import deque

bees = deque(int(x) for x in input().split())
bee_eaters = [int(x) for x in input().split()]

while bees and bee_eaters:
    bees_group = bees[0]
    bee_eaters_group = bee_eaters[-1]

    if bees_group < bee_eaters_group * 7:
        bees.popleft()
        bee_eaters.pop()
        removed_eaters = bees_group // 7
        survived_eaters = bee_eaters_group - removed_eaters
        bee_eaters.append(survived_eaters)
    elif bees_group > bee_eaters_group * 7:
        bees.popleft()
        bee_eaters.pop()
        survived_bees = bees_group - (bee_eaters_group * 7)
        bees.append(survived_bees)
    elif bees_group == bee_eaters_group * 7:
        bees.popleft()
        bee_eaters.pop()

print("The final battle is over!")
if not bees and not bee_eaters:
    print("But no one made it out alive!")
elif bees and not bee_eaters:
    print(f"Bee groups left: {', '.join(str(x) for x in bees)}")
elif bee_eaters and not bees:
    print(f"Bee-eater groups left: {', '.join(str(x) for x in bee_eaters)}")
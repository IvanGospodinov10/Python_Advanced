from collections import deque

substances  = [int(x) for x in input().split(", ")]
crystals = deque(int(x) for x in input().split(", "))

potions_to_craft = {
    110: "Brew of Immortality",
    100: "Essence of Resilience",
    90: "Draught of Wisdom",
    80: "Potion of Agility",
    70: "Elixir of Strength"
}

potions_to_craft = dict(sorted(potions_to_craft.items(), key=lambda x: x[0]))

crafted_potions = []

while substances and crystals and len(crafted_potions) < 5:

    substance = substances.pop()
    crystal_energy = crystals.popleft()

    points = substance + crystal_energy

    if points in potions_to_craft and potions_to_craft[points] not in crafted_potions:
        crafted_potions.append(potions_to_craft[points])
        continue

    try_to_craft_potion = []
    for en, p_name in potions_to_craft.items():
        if en < points and p_name not in crafted_potions:
            try_to_craft_potion.append(en)

    if try_to_craft_potion:
        max_potion_to_craft = max(try_to_craft_potion)
        crafted_potions.append(potions_to_craft[max_potion_to_craft])
        crystal_energy -= 20
        if crystal_energy > 0:
            crystals.append(crystal_energy)

    else:
        crystal_energy -= 5
        if crystal_energy > 0:
            crystals.append(crystal_energy)

if len(crafted_potions) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")
if crafted_potions:
    print(f"Crafted potions: {', '.join(crafted_potions)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances[::-1])}")
if crystals:
    print(f"Crystals: {', '.join(str(x) for x in crystals)}")

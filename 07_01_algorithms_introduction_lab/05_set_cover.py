def set_cover(universe, sets):
    universe_set = set(universe)
    chosen_sets = []

    while universe_set:
        best_set = max(sets, key=lambda s: len(s & universe_set))
        chosen_sets.append(best_set)
        universe_set -= best_set

    return chosen_sets


universe = [int(x.strip()) for x in input().split(",")]
n = int(input())

sets = []
for _ in range(n):
    current = {int(x.strip()) for x in input().split(",")}
    sets.append(current)

chosen = set_cover(universe, sets)

print(f"Sets to take ({len(chosen)}):")
for s in chosen:
    print(f"{{ {', '.join(str(x) for x in sorted(s))} }}")

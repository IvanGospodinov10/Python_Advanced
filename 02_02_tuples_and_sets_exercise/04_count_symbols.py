some_text = tuple(x for x in input())

data = {}

for character in some_text:
    if character not in data:
        data[character] = some_text.count(character)

sorted_data = dict(sorted(data.items()))


for character, count in sorted_data.items():
    print(f"{character}: {count} time/s")

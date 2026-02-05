with open("text.txt") as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            for chr in "{-,.!?":
                line = line.replace(chr, '@')
            print(" ".join(reversed(line.split())))

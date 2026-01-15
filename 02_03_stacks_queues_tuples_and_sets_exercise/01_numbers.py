first_numbers = set(int(x) for x in input().split())
second_numbers = set(int(x) for x in input().split())


for _ in range(int(input())):
    line = input().split()
    command = line[0] + " " + line[1]
    numbers = [int(x) for x in line[2:]]

    if command == "Add First":
        first_numbers.update(numbers)
    elif command == "Add Second":
        second_numbers.update(numbers)
    elif command == "Remove First":
         first_numbers.difference_update(numbers)
    elif command == "Remove Second":
        second_numbers.difference_update(numbers)
    elif command == "Check Subset":
        print(first_numbers.issubset(second_numbers) or second_numbers.issubset(first_numbers))

print(*sorted(first_numbers), sep=", ")
print(*sorted(second_numbers), sep=", ")


numbers = input().split()

# reversed_numbers = []
# for number in range(len(numbers)):
#     last_number = numbers.pop()
#     reversed_numbers.append(last_number)
# print(" ".join(reversed_numbers))

while numbers:
    print(f"{numbers.pop()}", end=' ')
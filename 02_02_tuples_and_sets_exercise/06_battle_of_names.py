odd_names = set()
even_names = set()

for index in range(1, int(input()) + 1):
    current_name = sum(ord(char) for char in input()) // index
    if current_name % 2 == 0:
        even_names.add(current_name)
    else:
        odd_names.add(current_name)

odd_sum = sum(odd_names)
even_sum = sum(even_names)

if odd_sum == even_sum:
    result = odd_names | even_names
elif odd_sum > even_sum:
    result = odd_names - even_names
else:
    result = even_names ^ odd_names

print(", ".join(str(x) for x in result))

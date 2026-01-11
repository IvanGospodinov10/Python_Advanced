def create_set_from_range(range_num):
    start, end = range_num.split(",")
    result = set(num for num in range(int(start), int(end) + 1))
    # for num in range(int(start), int(end) + 1):
    #     result.add(num)

    return result


longest_intersection = set()

for _ in range(int(input())):
    first_range, second_range = input().split("-")

    set_1 = create_set_from_range(first_range)
    set_2 = create_set_from_range(second_range)

    current_intersection = set_1.intersection(set_2)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")


n = int(input())

# matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
#
# flattened_matrix = [num for sublist in matrix for num in sublist]
# print(flattened_matrix)

nums = []

for i in range(n):
    data = [int(el) for el in input().split(", ")]
    nums.extend(data)

print(nums)


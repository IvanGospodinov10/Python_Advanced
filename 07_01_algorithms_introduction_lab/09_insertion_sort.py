def insertion_sort(nums):
    for j in range(1, len(nums)):
        for i in range(j, 0, -1):
            if nums[i] < nums[i-1]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
            else:
                break



nums_array = [int(x) for x in input().split()]
insertion_sort(nums_array)
print(*nums_array)
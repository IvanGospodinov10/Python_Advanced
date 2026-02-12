def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid_index = (left + right) // 2

        mid_el = array[mid_index]
        if mid_el == target:
            return mid_index
        if mid_el < target:
            left = mid_index + 1
        else:
            right = mid_index - 1

    return -1



nums = [int(x) for x in input().split()]
target_search = int(input())
print(binary_search(nums, target_search))
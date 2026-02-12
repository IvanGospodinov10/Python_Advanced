def calc_sum(_numbers, index):
    if index == len(_numbers) - 1:
        return _numbers[index]

    return _numbers[index] + calc_sum(_numbers, index + 1)


numbers = [int(x) for x in input().split()]
print(calc_sum(numbers, 0))
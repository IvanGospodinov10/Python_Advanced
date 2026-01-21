from functools import reduce


def sum_num(*args: int) -> int:
    return reduce(lambda x, y: x + y, args)


def sub_num(*args: int) -> int:
    return reduce(lambda x, y: x - y, args)


def mul_num(*args: int) -> int:
    return reduce(lambda x, y: x * y, args)


def div_num(*args: int) -> int:
    return reduce(lambda x, y: x / y, args)


mapper = {
    "+": sum_num,
    "-": sub_num,
    "*": mul_num,
    "/": div_num
}


def operate(sign, *args):
    func = mapper[sign]
    return func(*args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))

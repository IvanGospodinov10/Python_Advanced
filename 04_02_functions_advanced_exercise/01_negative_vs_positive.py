def numbers_sum(*args):
    pos_sum = 0
    neg_sum = 0

    for n in args:
        if n > 0:
            pos_sum += n
        else:
            neg_sum += n
    result = [str(neg_sum), str(pos_sum)]

    if abs(neg_sum) > abs(pos_sum):
        result.append("The negatives are stronger than the positives")
    else:
        result.append("The positives are stronger than the negatives")

    return "\n".join(result)


num = map(int, input().split())
print(numbers_sum(*num))

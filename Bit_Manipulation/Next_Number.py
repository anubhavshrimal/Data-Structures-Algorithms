# Find the next greater and next smaller number with same number of set bits


def next_greater(num):
    res = num
    if num != 0:
        right_one = num & -num
        left_pattern = num + right_one
        right_pattern = (num ^ left_pattern) >> (right_one + 1)
        res = left_pattern | right_pattern

    return res


def next_smaller(num):
    return ~next_greater(~num)


print(next_greater(6))
print(next_smaller(6))

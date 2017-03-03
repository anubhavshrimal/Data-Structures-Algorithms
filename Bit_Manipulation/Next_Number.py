# Find the next greater and next smaller number with same number of set bits

# Ex. num = 6 bin = 110
def next_greater(num):
    res = num
    if num != 0:
        # Find the right most 1 position
        # Ex. right_one = 2 bin = 10
        right_one = num & -num

        # get the left pattern to merge
        # Ex. left_pattern = 8 bin = 1000
        left_pattern = num + right_one

        # get the right patten to merge
        # Ex. right_pattern = 1 bin = 0001
        right_pattern = (num ^ left_pattern) >> (right_one + 1)

        # OR both the patterns
        # Ex. res = 0 bin = 1001
        res = left_pattern | right_pattern

    return res


def next_smaller(num):
    return ~next_greater(~num)


print(next_greater(6))
print(next_smaller(6))

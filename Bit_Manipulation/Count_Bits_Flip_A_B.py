# Count number of bits needed to be flipped to convert A to B


def count_bits_flip(a, b):
    # XOR a and b to get 1 on opposite value bit position
    c = a ^ b

    # initialise the counter for 1
    count = 0

    # count the number of 1s while there is 1 in a ^ b
    while c != 0:
        count += 1
        c &= (c-1)

    # return the count of 1s
    return count


# 2 = 0010
# 8 = 1000
print(count_bits_flip(2, 8))

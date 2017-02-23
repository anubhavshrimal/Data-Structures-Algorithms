# Count number of bits needed to be flipped to convert A to B


def count_bits_flip(a, b):
    return bin(a ^ b).count("1")

# 2 = 0010
# 8 = 1000
print(count_bits_flip(2, 8))

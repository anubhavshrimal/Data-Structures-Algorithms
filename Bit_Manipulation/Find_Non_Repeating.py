# Find the two non-repeating elements in an array of repeating elements


def find_non_repeating_numbers(arr):
    xor = arr[0]

    for i in range(1, len(arr)):
        xor ^= arr[i]

    right_set_bit = xor & ~(xor-1)
    first = 0
    second = 0
    for i in arr:
        if i & right_set_bit:
            first ^= i
        else:
            second ^= i

    return first, second


arr = [2, 3, 7, 9, 11, 2, 3, 11]
print(find_non_repeating_numbers(arr))

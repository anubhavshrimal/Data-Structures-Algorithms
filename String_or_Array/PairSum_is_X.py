# Find a pair of elements in the array with sum = x

"""
Method 1: If unsorted array
Time Complexity: O(n)
Space Complexity: O(n)
"""


def find_pair_unsorted(arr, x):
    elem_set = set({})

    # To store the indexes of both the elements
    pair = [-1, -1]

    for value in arr:
        # if x - value has already been discovered in the array
        # Pair found, return the values
        if (x-value) in elem_set:
            return x-value, value
        
        # else add the current value in the elem_set
        else:
            elem_set.add(value)

    return "Not found"

arr = [1, 4, 45, 6, 10, 8]
print('Unsorted array:', arr)
print('Pair with sum 16 in unsorted array:', find_pair_unsorted(arr, 16))


"""
Method 2: If array is sorted
Time Complexity: O(n)
Space Complexity: O(1)
"""

def find_pair_sorted(arr, x):
    # initialize variables to the start and end of the array
    l = 0
    r = len(arr) - 1

    while l < r:
        pair_sum = arr[l] + arr[r]

        # if pair is found
        if pair_sum == x:
            return arr[l], arr[r]
        # if the pair sum is less than x go to the next bigger value from left
        elif pair_sum < x:
            l += 1
        # if the pair sum is more than x go to the next lesser value from right
        else:
            r -= 1

    # If pair not found
    return "Not found"


arr = [2, 6, 10, 15, 18, 20, 23, 25]
print('Sorted array:', arr)
print('Pair with sum 28 in sorted array:', find_pair_sorted(arr, 28))

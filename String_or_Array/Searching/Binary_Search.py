# Function for binary search
# inputs: sorted array 'arr', key to be searched 'x'
# returns: index of the occurrence of x found in arr


def binary_search(arr, x):
    l = 0
    r = len(arr)

    # while the left index marker < right index marker
    while l < r:
        # find the index of the middle element
        mid = int(l + ((r - l) / 2))

        # if middle element is x, return mid
        if arr[mid] == x:
            return mid

        # if middle element is < x, update l to search to the right of mid
        elif arr[mid] < x:
            l = mid + 1

        # if middle element is > x, update r to search to the left of mid
        else:
            r = mid - 1

    return -1


arr = [1, 4, 5, 7, 8, 10, 13, 15]
print(binary_search(arr, 5))

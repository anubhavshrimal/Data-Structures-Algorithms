# Find the Kth smallest element in a given array.
# taking smallest in arr as 1st smallest

"""
Approach used: QuickSelect
Time Complexity: O(n)
"""


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_select(arr, low, high, k):
    # arr follows zero indexing hence kth smallest will be at index (k - 1)
    k -= 1
    while low < high:
        p_index = partition(arr, low, high)

        # found the kth smallest value
        if p_index == k:
            return arr[p_index]
        # pivot index is less than k hence kth smallest is in the right half
        elif p_index < k:
            low = p_index + 1
        # pivot index is greater than k hence kth smallest is in the left half
        else:
            high = p_index - 1
    # if k < 0 or k > len(arr) then simply return the smallest or largest value in arr
    return arr[low]


arr = [10, 7, 8, 9, 1, 5]
n = len(arr) - 1

# find 4th smallest element in the array
print(quick_select(arr, 0, n, 4))



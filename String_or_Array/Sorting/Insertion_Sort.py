def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            # copy value of previous index to index + 1
            arr[j + 1] = arr[j]
            # j = j - 1
            j -= 1
        # copy the value which was at ith index to its correct sorted position
        arr[j + 1] = x


arr = [12, 11, 13, 5, 6]
print('Before sort arr: ', arr)
insertion_sort(arr)
print('Sorted arr: ', arr)

"""
Output:
Before sort arr:  [12, 11, 13, 5, 6]
Sorted arr:  [5, 6, 11, 12, 13]
"""
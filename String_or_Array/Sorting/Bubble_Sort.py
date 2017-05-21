# bubble sort function
def bubble_sort(arr):
    n = len(arr)

    # Repeat loop N times
    # equivalent to: for(i = 0; i < n-1; i++)
    for i in range(0, n-1):
        # Repeat internal loop for (N-i)th largest element
        for j in range(0, n-i-1):

            # if jth value is greater than (j+1) value
            if arr[j] > arr[j+1]:
                # swap the values at j and j+1 index
                # Pythonic way to swap 2 variable values -> x, y = y, x
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]
print('Before sorting:', arr)

# call bubble sort function on the array
bubble_sort(arr)

print('After sorting:', arr)

"""
Output:
Before sorting: [64, 34, 25, 12, 22, 11, 90]
After sorting: [11, 12, 22, 25, 34, 64, 90]
"""
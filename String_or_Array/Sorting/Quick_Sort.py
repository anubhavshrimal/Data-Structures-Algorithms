# Python program for implementation of Quicksort Sort by taking last element as pivot


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


# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pivot is set to its right position after partition call
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
print("Before sorting array is:")
for i in range(n):
    print(arr[i], end=' -> ')
print('end')

quickSort(arr, 0, n - 1)

print("Sorted array is:")
for i in range(n):
    print(arr[i], end=' -> ')
print('end')

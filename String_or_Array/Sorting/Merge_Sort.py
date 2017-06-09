# Program to perform merge sort on an array


def merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid

    # create temporary arrays
    """
    arr = [0] * n is equivalent to:
    arr = [0, 0, 0, ..., 0]
    array of n zeros
    """
    arr1 = [0] * n1
    arr2 = [0] * n2

    # copy data of arr into arr1 and arr2
    for i in range(0, n1):
        arr1[i] = arr[low + i]

    for i in range(0, n2):
        arr2[i] = arr[mid + 1 + i]

    # initialize i, j to 0
    i = j = 0

    # initialize k to lower index
    k = low

    # merge the 2 arrays
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    # if elements left in arr1 copy them to arr
    while i < n1:
        arr[k] = arr1[i]
        i += 1
        k += 1

    # if elements left in arr2 copy them to arr
    while j < n2:
        arr[k] = arr2[j]
        j += 1
        k += 1


def merge_sort(arr, low, high):
    if low < high:
        # mid = int((low + high) / 2)
        mid = int(low + ((high - low) / 2))

        # call merge_sort on 2 halves
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)

        # merge the two sorted halves
        merge(arr, low, mid, high)


arr = [5, 21, 7, 3, 4, 8, 9, 10, 100, 15]

print('Before merge sort:', arr)

# Call merge sort on arr
merge_sort(arr, 0, len(arr)-1)

print('After merge sort:', arr)

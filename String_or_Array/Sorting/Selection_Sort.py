# selection sort function
def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(i+1, n):
            # if the value at i is > value at j -> swap
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


# input arr
arr = [3, 2, 4, 1, 5]
print('Before selection sort:', arr)

# call selection sort function
selection_sort(arr)
print('After selection sort:', arr)

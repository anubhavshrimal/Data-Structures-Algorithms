# counting sort without stable sorting


def counting_sort(arr):
    n = len(arr)

    # get the maximum value of the array
    max_val = max(arr)

    count = [0] * (max_val + 1)

    # fill the count array
    # for each element x in the array
    for x in arr:
        count[x] += 1

    k = 0
    for i in range(0, len(count)):
        for j in range(0, count[i]):
            arr[k] = i
            k += 1


arr = [3, 2, 1, 3, 2, 5, 5, 3]
print('Before counting sort:', arr)

# call counting sort function
counting_sort(arr)

print('After counting sort:', arr)

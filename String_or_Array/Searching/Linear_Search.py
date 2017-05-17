

# Function for linear search
# inputs: array of elements 'arr', key to be searched 'x'
# returns: index of first occurrence of x in arr
def linear_search(arr, x):
    # traverse the array
    for i in range(0, len(arr)):

        # if element at current index is same as x
        # return the index value
        if arr[i] == x:
            return i

    # if the element is not found in the array return -1
    return -1

arr = [3, 2, 1, 5, 6, 4]
print(linear_search(arr, 1))

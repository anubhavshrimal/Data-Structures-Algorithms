"""A max heap is a complete binary tree [CBT] (implemented using array)
in which each node has a value larger than its sub-trees"""

from math import ceil


def max_heapify(indx, arr, size):
    """
    Assuming sub trees are already max heaps, converts tree rooted at current indx into a max heap.
    :param indx: Index to check for max heap
    :param arr: array of elements
    :param size: size of the array
    """

    # Get index of left and right child of indx node
    left_child = indx * 2 + 1
    right_child = indx * 2 + 2

    largest = indx

    # check what is the largest value node in indx, left child and right child
    if left_child < size:
        if arr[left_child] > arr[largest]:
            largest = left_child
    if right_child < size:
        if arr[right_child] > arr[largest]:
            largest = right_child

    # if indx node is not the largest value, swap with the largest child
    # and recursively call max_heapify on the respective child swapped with
    if largest != indx:
        arr[indx], arr[largest] = arr[largest], arr[indx]
        max_heapify(largest, arr, size)


def insert(value, arr):
    """
    Inserts an element in the max heap
    :param value: value to be inserted in the heap
    :param arr: already present max heap
    :return: new max heap with inserted value
    """
    arr.append(value)
    size = len(arr)

    indx = size - 1

    # Get parent index of the current node
    parent = int(ceil(indx/2 - 1))

    # Check if the parent value is smaller than the newly inserted value
    # if so, then replace the value with the parent value and check with the new parent
    while parent >= 0 and arr[indx] > arr[parent]:
        arr[indx], arr[parent] = arr[parent], arr[indx]
        indx = parent
        parent = int(ceil(indx / 2 - 1))

    return arr


def delete(indx, arr):
    """
    Deletes the value on the specified index node
    :param indx: index whose node is to be removed
    :param arr: max heap
    :return: Value of the node deleted from the heap
    """

    arr[-1], arr[indx] = arr[indx], arr[-1]
    heap_size = len(arr) - 1

    max_heapify(indx, arr, heap_size)

    return arr.pop()


def extract_max(arr):
    """
    Extracts the maximum value from the heap
    :param arr: max heap
    :return: extracted max value
    """
    return delete(0, arr)


def create_max_heap(arr):
    """
    Converts a given array into a max heap
    :param arr: input array of numbers
    :return: output max heap
    """
    n = len(arr)

    # last n/2 elements will be leaf nodes (CBT property) hence already max heaps
    # loop from n/2 to 0 index and convert each index node into max heap
    for i in range(int(n/2), -1, -1):
        max_heapify(i, arr, n)

    return arr


heap = [5, 10, 4, 8, 3, 0, 9, 11]
heap = create_max_heap(heap)
insert(15, heap)
print(delete(2, heap))
print(extract_max(heap))
print(*heap)

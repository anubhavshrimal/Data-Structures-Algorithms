"""Perform Sorting using a max heap in:
O(n log n) time complexity
O(1) space complexity"""


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


def heap_sort(arr):
    """
    Sorts the given array using heap sort
    :param arr: input array to sort
    """

    create_max_heap(arr)
    heap_size = len(arr)

    # Swap the max value in heap with the end of the array and decrease the size of the heap by 1
    # call max heapify on the 0th index of the array
    while heap_size > 1:
        arr[heap_size-1], arr[0] = arr[0], arr[heap_size-1]
        heap_size -= 1
        max_heapify(0, arr, heap_size)


heap = [5, 10, 4, 8, 3, 0, 9, 11]
heap_sort(heap)
print(*heap)

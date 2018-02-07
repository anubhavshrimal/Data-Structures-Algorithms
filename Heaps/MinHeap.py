"""A Min heap is a complete binary tree [CBT] (implemented using array)
in which each node has a value smaller than its sub-trees"""

from math import ceil


class MinHeap:
    def __init__(self, arr=None):
        self.heap = []
        self.heap_size = 0
        if arr is not None:
            self.create_min_heap(arr)
            self.heap = arr
            self.heap_size = len(arr)

    def create_min_heap(self, arr):
        """
        Converts a given array into a min heap
        :param arr: input array of numbers
        """
        n = len(arr)

        # last n/2 elements will be leaf nodes (CBT property) hence already min heaps
        # loop from n/2 to 0 index and convert each index node into min heap
        for i in range(int(n / 2), -1, -1):
            self.min_heapify(i, arr, n)

    def min_heapify(self, indx, arr, size):
        """
        Assuming sub trees are already min heaps, converts tree rooted at current indx into a min heap.
        :param indx: Index to check for min heap
        """
        # Get index of left and right child of indx node
        left_child = indx * 2 + 1
        right_child = indx * 2 + 2

        smallest = indx

        # check what is the smallest value node in indx, left child and right child
        if left_child < size:
            if arr[left_child] < arr[smallest]:
                smallest = left_child
        if right_child < size:
            if arr[right_child] < arr[smallest]:
                smallest = right_child

        # if indx node is not the smallest value, swap with the smallest child
        # and recursively call min_heapify on the respective child swapped with
        if smallest != indx:
            arr[indx], arr[smallest] = arr[smallest], arr[indx]
            self.min_heapify(smallest, arr, size)

    def insert(self, value):
        """
        Inserts an element in the min heap
        :param value: value to be inserted in the heap
        """
        self.heap.append(value)
        self.heap_size += 1

        indx = self.heap_size - 1

        # Get parent index of the current node
        parent = int(ceil(indx / 2 - 1))

        # Check if the parent value is smaller than the newly inserted value
        # if so, then replace the value with the parent value and check with the new parent
        while parent >= 0 and self.heap[indx] < self.heap[parent]:
            self.heap[indx], self.heap[parent] = self.heap[parent], self.heap[indx]
            indx = parent
            parent = int(ceil(indx / 2 - 1))

    def delete(self, indx):
        """
        Deletes the value on the specified index node
        :param indx: index whose node is to be removed
        :return: Value of the node deleted from the heap
        """
        if self.heap_size == 0:
            print("Heap Underflow!!")
            return

        self.heap[-1], self.heap[indx] = self.heap[indx], self.heap[-1]
        self.heap_size -= 1

        self.min_heapify(indx, self.heap, self.heap_size)

        return self.heap.pop()

    def extract_min(self):
        """
        Extracts the minimum value from the heap
        :return: extracted min value
        """
        return self.delete(0)

    def print(self):
        print(*self.heap)


heap = MinHeap([5, 10, 4, 8, 3, 0, 9, 11])

heap.insert(15)
print(heap.delete(2))
print(heap.extract_min())
heap.print()

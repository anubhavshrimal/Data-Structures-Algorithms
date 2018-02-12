"""
Given an input stream of  integers, you must perform the following task for each i-th integer:

1. Add the i-th integer to a running list of integers.
2. Find the median of the updated list (i.e., for the first element through the i-th element).
3. Print the list's updated median on a new line.

*) Input Format
    The first line contains a single integer, n, denoting the number of integers in the data stream.
    Each line i of the n subsequent lines contains an integer, ai, to be added to your list.
*) Output Format
    After each new integer is added to the list, print the list's updated median on a new line.
Example:
Input:
    6
    12
    4
    5
    3
    8
    7
Output:
    12.0
    8.0
    5.0
    4.5
    5.0
    6.0
Problem Link: https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem
"""

"""A max heap is a complete binary tree [CBT] (implemented using array)
in which each node has a value larger than its sub-trees"""

from math import ceil


class MaxHeap:
    def __init__(self, arr=None):
        self.heap = []
        self.heap_size = 0
        if arr is not None:
            self.create_max_heap(arr)
            self.heap = arr
            self.heap_size = len(arr)

    def create_max_heap(self, arr):
        """
        Converts a given array into a max heap
        :param arr: input array of numbers
        """
        n = len(arr)

        # last n/2 elements will be leaf nodes (CBT property) hence already max heaps
        # loop from n/2 to 0 index and convert each index node into max heap
        for i in range(int(n / 2), -1, -1):
            self.max_heapify(i, arr, n)

    def max_heapify(self, indx, arr, size):
        """
        Assuming sub trees are already max heaps, converts tree rooted at current indx into a max heap.
        :param indx: Index to check for max heap
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
        # and recursively call min_heapify on the respective child swapped with
        if largest != indx:
            arr[indx], arr[largest] = arr[largest], arr[indx]
            self.max_heapify(largest, arr, size)

    def insert(self, value):
        """
        Inserts an element in the max heap
        :param value: value to be inserted in the heap
        """
        self.heap.append(value)
        self.heap_size += 1

        indx = self.heap_size - 1

        # Get parent index of the current node
        parent = int(ceil(indx / 2 - 1))

        # Check if the parent value is smaller than the newly inserted value
        # if so, then replace the value with the parent value and check with the new parent
        while parent >= 0 and self.heap[indx] > self.heap[parent]:
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

        self.max_heapify(indx, self.heap, self.heap_size)

        return self.heap.pop()

    def extract_max(self):
        """
        Extracts the maximum value from the heap
        :return: extracted max value
        """
        return self.delete(0)

    def max(self):
        return self.heap[0]


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

    def min(self):
        return self.heap[0]


"""
Algorithm:
*) Split the array stream in 2 halves, min heap(upper array) and max heap (lower array)
*) This was the min and max of the heaps will help you get the median fast.
*) Note that the elements should be inserted in the heaps in such a way that the elements 
in lowerMaxHeap are all smaller than all the elements in the upperMinHeap 
(i.e., as if the arrays were sorted and then split into two heaps)
"""
n = int(input())
upperMinHeap = MinHeap()
lowerMaxHeap = MaxHeap()

for a_i in range(1, n+1):
    a_t = int(input())

    if lowerMaxHeap.heap_size == 0:  # this case occurs only initially when both heaps are empty
        lowerMaxHeap.insert(a_t)
    else:
        # Take example stream 1,2,3,4,9,8,7,6,5 to understand the logic
        if upperMinHeap.heap_size == lowerMaxHeap.heap_size:
            if a_t > upperMinHeap.min():
                temp = upperMinHeap.extract_min()
                lowerMaxHeap.insert(temp)
                upperMinHeap.insert(a_t)
            else:
                lowerMaxHeap.insert(a_t)
        elif a_t > lowerMaxHeap.max():
            upperMinHeap.insert(a_t)
        else:
            temp = lowerMaxHeap.extract_max()
            upperMinHeap.insert(temp)
            lowerMaxHeap.insert(a_t)

    # print the median directly if odd number of elements
    # otherwise average of sum of min heap and max heap tops
    num = a_i / 2
    if int(num) != num:
        print(float(lowerMaxHeap.max()))
    else:
        print((lowerMaxHeap.max() + upperMinHeap.min()) / 2)

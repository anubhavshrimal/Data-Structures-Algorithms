"""Given an array arr of length n where each element is at most k places away from its sorted position,
Code an efficient algorithm to sort arr.
"""
import heapq

def kHeapSort(arr, k):
    h = []
    n = len(arr)
    for i in range(0, k+1):
      heapq.heappush(h, arr[i])
    for i in range(k+1, n):
        arr[i-(k+1)] = heapq.heappop(h)
        heapq.heappush(h, arr[i])
    for i in range(0, k+1):
     arr[n-k-1 + i] = heapq.heappop(h)
    return arr

if __name__ == '__main__':
    arr = [2, 1, 4, 3, 6, 5]

    print(kHeapSort(arr, 2))

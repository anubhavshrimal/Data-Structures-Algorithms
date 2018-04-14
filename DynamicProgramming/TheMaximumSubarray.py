# HackerRank problem Algorithms DP


def maxSubArray(a, size):
    currMax = a[0]
    maxSoFar = a[0]

    for i in range(1, size):
        currMax = max(a[i], currMax + a[i])
        maxSoFar = max(currMax, maxSoFar)

    return maxSoFar


testcases = int(input())

for t in range(testcases):
    n = int(input())
    arr = list(map(int, input().split()))
    tempList = list(filter(lambda x: x > 0, arr))
    if len(tempList) != 0:
        maximumSum = sum(tempList)
    else:
        maximumSum = max(arr)
    print(maxSubArray(arr, n), maximumSum)

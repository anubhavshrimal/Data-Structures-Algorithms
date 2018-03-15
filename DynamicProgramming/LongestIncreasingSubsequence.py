"""
Find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted
in increasing order.
For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.
"""


def lis(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = 1 + dp[j]

    return max(dp)


arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(lis(arr))

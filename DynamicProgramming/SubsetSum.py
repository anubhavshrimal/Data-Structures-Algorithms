"""
Given a set of non-negative integers, and a value sum,
determine if there is a subset of the given set with sum equal to given sum.
"""


def isSubsetSum(arr, check_sum):
    n = len(arr)
    possible_sum = [[False] * (n + 1) for _ in range(check_sum + 1)]

    for i in range(n+1):
        possible_sum[0][i] = True

    for i in range(1, check_sum + 1):
        for j in range(1, n + 1):
            if i < arr[j - 1]:
                possible_sum[i][j] = possible_sum[i][j-1]
            elif i >= arr[j - 1]:
                possible_sum[i][j] = possible_sum[i][j-1] or possible_sum[i - arr[j - 1]][j-1]

    return possible_sum[check_sum][n]


arr = [3, 34, 4, 12, 5, 2]
check_sum = 9

if isSubsetSum(arr, check_sum):
    print("Found a subset with sum =", check_sum)
else:
    print("Subset with sum =", check_sum, "Not Found")



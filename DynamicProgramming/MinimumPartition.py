# Partition a set into two subsets such that the difference of subset sums is minimum


def find_min(arr):
    sum_of_arr = sum(arr)
    n = len(arr)
    dp = [[False for i in range(sum_of_arr+1)] for i in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True

    for i in range(1, sum_of_arr+1):
        dp[0][i] = False

    for i in range(1, n+1):
        for j in range(1, sum_of_arr+1):
            dp[i][j] = dp[i-1][j]

            if arr[i-1] <= j:
                dp[i][j] |= dp[i-1][j - arr[i-1]]

    diff = float('inf')

    for j in range(int(sum_of_arr/2), -1, -1):
        if dp[n][j] is True:
            diff = sum_of_arr - 2 * j
            break

    return diff


if __name__ == '__main__':
    arr = [3, 1, 4, 2, 2, 1]
    print("Minimum difference is:", find_min(arr))
"""Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n.
Determine the maximum value obtainable by cutting up the rod and selling the pieces."""


def cutting_rod(prices, n):
    dp = [0 for i in range(n+1)]
    dp[0] = 0

    for i in range(1, n+1):
        max_val = -float('inf')
        for j in range(i):
            max_val = max(max_val, prices[j] + dp[i-j-1])
        dp[i] = max_val

    return dp[n]


if __name__ == '__main__':
    arr = [1, 5, 8, 9, 10, 17, 17, 20]
    size = len(arr)
    print("Maximum Obtainable Value is " + str(cutting_rod(arr, size)))

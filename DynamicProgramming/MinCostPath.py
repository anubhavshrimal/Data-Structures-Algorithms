"""Given a cost matrix cost[][] and a position (m, n) in cost[][],
write a function that returns cost of minimum cost path to reach (m, n) from (0, 0).
Total cost of a path to reach (m, n) is sum of all the costs on that path (including both source and destination).
You can only traverse down, right and diagonally lower cells from a given cell"""


def min_cost(cost, m, n):
    dp = [[0 for i in range(n+1)] for i in range(m+1)]

    dp[0][0] = cost[0][0]

    for i in range(1, m+1):
        dp[i][0] = dp[i-1][0] + cost[i][0]

    for j in range(1, n+1):
        dp[0][j] = dp[0][j-1] + cost[0][j]

    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = cost[i][j] + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m][n]


if __name__ == '__main__':
    cost = [[1, 2, 3],
            [4, 8, 2],
            [1, 5, 3]]
    m = 2
    n = 2
    print("Minimum cost from (0, 0) to ({}, {}) is:".format(m, n), min_cost(cost, m, n))

"""Given weights and values of n items, put these items in a knapsack of capacity W to get
the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1]
and wt[0..n-1] which represent values and weights associated with n items respectively. Also
given an integer W which represents knapsack capacity, find out the maximum value subset of val[]
such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item,
either pick the complete item, or don’t pick it (0-1 property)."""


def knapSack(W, wt, val, size):
    k = [[0 for i in range(W+1)] for i in range(size+1)]
    for i in range(size+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                k[i][w] = 0
            elif wt[i-1] <= w:
                k[i][w] = max(val[i-1] + k[i-1][w-wt[i-1]], k[i-1][w])
            else:
                k[i][w] = k[i-1][w]

    for w in k:
        print(w)

    return k


# def findElementsInSack(W, matrix, wt, val, size):
#     i = size
#     row = W
#     arr = []
#     while i > 0:
#         print(matrix[i][row] - matrix[i-1][row - wt[i-1]] )
#         print(val[i-1])
#         if matrix[i][row] - matrix[i-1][row - wt[i-1]] == val[i-1]:
#             arr.append(val[i-1])
#             i -= 1
#             row -= wt[i-1]
#         else:
#             i -= 1
#
#     return arr

price = [60, 100, 120]
wt = [1, 2, 3]
W = 5
n = len(price)
k = knapSack(W, wt, price, n)
print(k[n][W])
# print(findElementsInSack(W, k, wt, price, n))

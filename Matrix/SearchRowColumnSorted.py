"""Given an n x n matrix, where every row and column is sorted in increasing order.
Given a number x, how to decide whether this x is in the matrix."""

def search(mat, x):
    n = len(mat)
    i = 0
    j = n-1
    while i < n and j >= 0:
        if mat[i][j] == x:
            return i, j
        elif mat[i][j] < x:
            i += 1
        else:
            j -= 1
    return [-1]


matrix = [[10, 20, 30, 40],
          [15, 25, 35, 45],
          [27, 29, 37, 48],
          [32, 33, 39, 50]
        ]

print("Enter element you want to search: ")
element = int(input())
index = search(matrix, element)
if len(index) == 1:
    print("Element not found")
else:
    print("element found at position:(", index[0], ",", index[1], ")")

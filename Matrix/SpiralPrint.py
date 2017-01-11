# Given a 2D array, print it in spiral form.
"""Input:
        1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
"""


def print_spiral(mat):
    row, col = len(mat), len(mat[0])
    k = 0
    l = 0
    while k < row and l < col:
        for i in range(col):
            print(mat[k][i], end=' ')
        k += 1

        for i in range(k, row):
            print(mat[i][col-1], end=' ')
        col -= 1

        if k < row:
            for i in reversed(range(l, col-1)):
                print(mat[row-1][i], end=' ')
            row -= 1

        if l < col:
            for i in reversed(range(k, row-1)):
                print(mat[i][l], end=' ')
            l += 1


a = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]
     ]

print_spiral(a)
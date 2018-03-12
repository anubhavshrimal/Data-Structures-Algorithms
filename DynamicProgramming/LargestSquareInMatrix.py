"""
Given a 2-D matrix of 0s and 1s, find the Largest Square which contains all 1s in itself.
"""


def find_largest_square(matrix):
    n = len(matrix)

    # make a matrix for storing the solutions
    cache = [[0] * n for _ in range(n)]
    # size of square and its bottom-right indexes
    size = 0
    right_indx = -1
    bottom_indx = -1

    for i in range(n):
        for j in range(n):

            # if the value is 0 simply move forward as it cannot form a square of 1s
            if matrix[i][j] == 0:
                continue

            # if it is first row or column, copy the matrix values as it is
            elif i == 0 or j == 0:
                cache[i][j] = matrix[i][j]

            # Otherwise, check in the up, left, and diagonally top-left direction for minimum size of square
            # if all are 1s at these positions in matrix, only then min value will be greater than 1
            # hence add the previous square size to the cache + 1
            else:
                cache[i][j] = 1 + min(cache[i - 1][j], cache[i][j - 1], cache[i - 1][j - 1])

            # check if the current square size found is larger than the previously found size, if so, update it
            if cache[i][j] > size:
                size = cache[i][j]
                bottom_indx, right_indx = i, j

    return size, bottom_indx, right_indx


mat = [[1, 1, 0, 1, 0],
       [0, 1, 1, 1, 0],
       [1, 1, 1, 1, 0],
       [0, 1, 1, 1, 1]]
size, bottom, right = find_largest_square(mat)

if size > 0:
    print("Size of the square:", size)
    print("Top-left Co-ordinates:", bottom-size+1, ",", right-size+1)
    print("Bottom-right Co-ordinates:", bottom, ",", right)
else:
    print("No square of 1s found")

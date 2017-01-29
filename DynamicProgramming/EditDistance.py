"""Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required
to convert ‘str1’ into ‘str2’.

Insert
Remove
Replace
All of the above operations are of equal cost.
Example:
Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically
need to convert "un" to "atur".  This can be done using
below three operations.
Replace 'n' with 'r', insert t, insert a"""


def edit_distance(str1, str2, m, n):
    matrix = [[0 for i in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):

            if i == 0:
                matrix[i][j] = j

            elif j == 0:
                matrix[i][j] = i

            elif str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]

            else:
                matrix[i][j] = 1 + min(matrix[i][j-1],      # insert
                                       matrix[i-1][j],      # remove
                                       matrix[i-1][j-1])    # replace

    return matrix[m][n]


if __name__ == '__main__':
    str1 = 'sunday'
    str2 = 'saturday'

    print(edit_distance(str1, str2, len(str1), len(str2)))
"""find the length of longest subsequence present in both of them.
 A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
 Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4."""


def lcs(str1, str2):
    m = len(str1)
    n = len(str2)

    matrix = [[0 for i in range(n+1)] for i in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):

            if i == 0 or j == 0:
                matrix[i][j] = 0

            elif str1[i-1] == str2[j-1]:
                matrix[i][j] = 1 + matrix[i-1][j-1]

            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    index = matrix[m][n]

    res = [""] * index
    i = m
    j = n

    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            res[index-1] = str1[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif matrix[i-1][j] > matrix[i][j-1]:
            i -= 1
        else:
            j -= 1

    return res


if __name__ == '__main__':
    X = "AGGTAB"
    Y = "GXTXAYB"

    str = ''.join(lcs(X, Y))

    print("Length of longest common subsequence is:", len(str),"\nAnd the subsequence is:", str)
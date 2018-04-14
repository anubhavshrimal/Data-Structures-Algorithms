# Find all possible words in a board of characters
"""Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
       boggle[][]   = {{'G','I','Z'},
                       {'U','E','K'},
                       {'Q','S','E'}};
Output:  Following words of dictionary are present
         GEEKS
         QUIZ
"""


def findWordsUtil(words, boggle, visited, found, r, c, str):
    rows = len(boggle)
    cols = len(boggle[0])

    # set the position of character as traversed
    visited[r][c] = True

    # add the character to string
    str += boggle[r][c]

    # if the string is in dictionary add it to the set of found words
    if str in words:
        found.add(str)

    # traverse all the nearby 8 adjacent cells
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if i >= rows or i < 0 or j >= cols or j < 0 or visited[i][j]:
                continue
            findWordsUtil(words, boggle, visited, found, i, j, str)

    # backtrack and set the status of current character as not traversed
    visited[r][c] = False


def findWords(words, boggle):
    rows = len(boggle)
    cols = len(boggle[0])

    # initialize a matrix for DFS Traversal
    visited = [[False for i in range(cols)] for j in range(rows)]

    # set to store the unique found words
    found = set({})
    str = ""

    # traverse each character in the boggle and do DFS from there
    for r in range(rows):
        for c in range(cols):
            findWordsUtil(words, boggle, visited, found, r, c, str)

    # return the set of found words
    return found

if __name__ == '__main__':
    words = {"GEEKS", "FOR", "QUIZ", "GO", "SEEK"}
    boggle = [['G', 'I', 'Z'],
              ['U', 'E', 'K'],
              ['Q', 'S', 'E']]

    found = findWords(words, boggle)

    print("Words found in the boggle from the dictionary are:")
    for word in found:
        print(word)

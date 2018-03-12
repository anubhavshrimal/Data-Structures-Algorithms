"""
Print all valid (properly opened and closed) combinations of n pairs of parentheses.
"""


def addParentheses(str_arr, leftParenCount, rightParenCount, combinations, index):
    if leftParenCount < 0 or rightParenCount < 0:
        return
    if leftParenCount == 0 and rightParenCount == 0:
        combinations.append(''.join(str_arr))
    else:
        if leftParenCount > 0:
            str_arr[index] = '('
            addParentheses(str_arr, leftParenCount - 1, rightParenCount, combinations, index + 1)
        
        if rightParenCount > leftParenCount:
            str_arr[index] = ')'
            addParentheses(str_arr, leftParenCount, rightParenCount - 1, combinations, index + 1)


def generateParentheses(count):
    str_arr = [''] * (count * 2)
    combinations = []
    addParentheses(str_arr, count, count, combinations, 0)
    return combinations


parenthesis_pairs = 3
combinations = generateParentheses(parenthesis_pairs)
print(*combinations, sep=', ')

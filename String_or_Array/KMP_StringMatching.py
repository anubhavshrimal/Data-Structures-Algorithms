# To find indexes of String "Pattern" in a given String "Text" using KMP Algorithm


# function that returns list of indexes where the patters matches
def KMP_Search(pattern, text):
    n = len(text)
    m = len(pattern)

    # pre-compute prefix array of the pattern
    prefix_arr = get_prefix_arr(pattern, m)

    # stores start point of pattern match in text
    start_points = []

    i = 0
    j = 0

    # while the whole text has not been searched
    while i != n:
        # if the character in text matches the pattern character
        if text[i] == pattern[j]:
            i += 1
            j += 1
        # else find the previous index from where the matching can resume
        else:
            j = prefix_arr[j-1]

        # if pattern length has been reached that means a pattern has been found
        if j == m:
            start_points.append(i-j)
            j = prefix_arr[j-1]
        elif j == 0:
            i += 1
    # return the starting position of pattern in text
    return start_points


# pre-computes the prefix array for KMP search
def get_prefix_arr(pattern, m):
    prefix_arr = [0] * m
    j = 0
    i = 1

    while i != m:
        if pattern[i] == pattern[j]:
            j += 1
            prefix_arr[i] = j
            i += 1
        elif j != 0:
                j = prefix_arr[j-1]
        else:
            prefix_arr[i] = 0
            i += 1

    return prefix_arr

txt = "ABABDABACDABABCABABCABAB"
pat = "ABABCABAB"

start_indexes = KMP_Search(pat, txt)

for i in start_indexes:
    print(i)

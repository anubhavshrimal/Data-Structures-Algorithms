# Find the longest substring with k unique characters in a given string


def longest_k_unique(string, k):
    unique = 0
    sets = set({})

    for i in string:
        if i not in sets:
            sets.add(i)
            unique += 1

    if unique < k:
        return -1, -1

    count = [0] * 26
    curr_end = curr_start = max_window_start = 0
    max_window_len = 1

    count[ord(string[0]) - ord('a')] += 1
    for i in range(1, len(string)):
        count[ord(string[i]) - ord('a')] += 1
        curr_end += 1

        while not isValid(count, k):
            count[ord(string[curr_start]) - ord('a')] -= 1
            curr_start += 1

        if curr_end - curr_start + 1 > max_window_len:
            max_window_len = curr_end - curr_start + 1
            max_window_start = curr_start

    return max_window_start, max_window_len


def isValid(count, k):
    val = 0
    for i in count:
        if i > 0:
            val += 1

    return k >= val


if __name__ == '__main__':
    string = 'aabaabab'
    k = 3
    max_start, max_len = longest_k_unique(string, k)

    if max_len == -1:
        print("K unique characters sub string does not exist.")
    else:
        print('max string with {} unique characters is "'.format(k) + string[max_start: max_start + max_len] +
              '" of length', max_len)

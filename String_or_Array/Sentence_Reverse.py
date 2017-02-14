"""[ 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

would turn into:
[ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't' ]"""


def reverse_sentence(arr):
    # reverse all characters:
    n = len(arr)
    mirrorReverse(arr, 0, n-1)

    # reverse each word:
    word_start = None
    for i in range(0, n):
        if arr[i] == " ":
            if word_start is not None:
                mirrorReverse(arr, word_start, i-1)
                word_start = None
        elif i == n-1:
            if word_start is not None:
                mirrorReverse(arr, word_start, i)
        else:
            if word_start is None:
                word_start = i


def mirrorReverse(arr, start, end):
    while start < end:
        tmp = arr[start]
        arr[start] = arr[end]
        arr[end] = tmp
        start += 1
        end -= 1


if __name__ == '__main__':
    arr = ['p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']

    print('Before reverse:', ''.join(arr))
    reverse_sentence(arr)
    print('After reverse: ', ''.join(arr))


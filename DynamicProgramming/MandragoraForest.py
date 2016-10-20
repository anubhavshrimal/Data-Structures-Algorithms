#HackerRank problem Algorithms DP


def maxExp(a, size):
    # if no mandragoras is eaten s = 1 and experience = sum(a)
    max_exp = curr_exp = sum_of_arr = sum(a)

    for i in range(size):
        # update the sum_of_arr by removing the value mandragoras eaten
        sum_of_arr -= a[i]
        # formula for experience after eating all mandragoras from 0 to i th position and fighting the remaining
        curr_exp = (curr_exp - (a[i] * (i+1))) + sum_of_arr
        max_exp = max(curr_exp, max_exp)

    return max_exp


testcases = int(input())

for t in range(testcases):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr) # sort the array
    print(maxExp(arr, n))
"""Given a distance ‘dist, count total number of ways to cover the distance with 1, 2 and 3 steps
Input:  n = 3
Output: 4
Below are the four ways
 1 step + 1 step + 1 step
 1 step + 2 step
 2 step + 1 step
 3 step"""


def count_ways(n):
    count = [0] * (n+1)
    count[0] = 1
    count[1] = 1
    count[2] = 2

    for i in range(3, n+1):
        count[i] = count[i-1] + count[i-2] + count[i-3]

    return count[n]


if __name__ == '__main__':
    print(count_ways(4))

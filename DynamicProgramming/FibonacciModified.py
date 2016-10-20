#HackerRank problem Algorithms DP

t1, t2, n = input().split()
t1 = int(t1)
t2 = int(t2)
n = int(n)

arr = [0]*n
arr[0] = t1
arr[1] = t2
for i in range(2, n):
    arr[i] = arr[i-2] + arr[i-1] ** 2

print(arr[-1])


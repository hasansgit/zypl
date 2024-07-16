m = int(input())
n = int(input())
d = float(input())
a = tuple(map(float, input().split()))
mt = [[0 for j in range(n)] for i in range(m)]

for i in range(m):
    mt[i][0] = a[i]

for i in range(m):
    for j in range(1, n):
        mt[i][j] = mt[i][j - 1] + d

for i in mt:
    print(*i)

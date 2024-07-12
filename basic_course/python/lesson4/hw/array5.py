n = int(input())
res = [1] * n
for i in range(2, n):
    res[i] = res[i - 1] + res[i - 2]
res = tuple(res)
print(res)

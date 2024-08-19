n = int(input())
a = list(map(int, input().split()))
k = 0
for i in a:
    if i % 2 == 1:
        print(i, end=' ')
        k += 1
print()
print(k)

a = list(map(int,input().split()))
x = 0
for i in range(1, len(a)):
    if a[i+x] != a[i-1+x]:
        a.insert(i + x,0)
        x += 1
a.append(0)
print(*a)

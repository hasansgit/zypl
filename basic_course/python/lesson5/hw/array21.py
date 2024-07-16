a = list(map(int, input().split()))
for i in range(9):
    if a[i] < a[9]:
        print(a[i])
        break
else:
    print(0)

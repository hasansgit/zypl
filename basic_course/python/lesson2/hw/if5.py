pos, neg = 0, 0

a = int(input())
b = int(input())
c = int(input())

if a > 0:
    pos += 1
elif a != 0:
    neg += 1
if b > 0:
    pos += 1
elif b != 0:
    neg += 1
if c > 0:
    pos += 1
elif c != 0:
    neg += 1

print(pos, neg)

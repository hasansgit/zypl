n = int(input())

while n > 0:
    if n % 10 == 2:
        print(True)
        break
    n //= 10
else:
    print(False)

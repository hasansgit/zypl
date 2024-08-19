def rect_ps(x1, y1, x2, y2):
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    print(2 * (a + b), a * b)


rect_ps(*map(float, input().split()))
rect_ps(*map(float, input().split()))
rect_ps(*map(float, input().split()))

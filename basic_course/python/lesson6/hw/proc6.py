def digit_count_sum(k):
    c, s = 0, 0
    while k:
        s += k % 10
        c += 1
        k //= 10
    print(c, s)


digit_count_sum(int(input()))
digit_count_sum(int(input()))
digit_count_sum(int(input()))

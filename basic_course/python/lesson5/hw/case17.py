n = int(input())
a = int(input())
b = int(input())
operation = {
    1: a + b,
    2: a - b,
    3: a * b,
    4: a / b,
}
print(operation[n])

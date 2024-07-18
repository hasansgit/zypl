import math as m
def my_function(a,b,c):
    p = (a + b + c) / 2
    s = m.sqrt(p*(p-a)*(p-b)*(p-c))
    return s

a = int(input())
b = int(input())
c = int(input())
print(my_function(a,b,c))

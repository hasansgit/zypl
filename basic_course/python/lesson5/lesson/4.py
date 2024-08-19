A = {'a','b','c','z'}
B = {'f','d','a','z'}

X = A.union(B)
print(X)
Y = A | B
print(Y)

X = A.intersection(B)
print(X)
Y = A & B
print(Y)

X = A.difference(B)
print(X)
Y = A - B
print(Y)

X = B.difference(A)
print(X)
Y = B - A
print(Y)

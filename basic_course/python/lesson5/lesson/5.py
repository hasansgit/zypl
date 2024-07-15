A = {'a','b','c','z'}
B = {'f','d','a','z'}

X = A.difference(B)
print('X => ',X)
print('A => ',A)

# A.difference_update(B)
A -= B
print('A => ',A)

print(A)
print(B)

A.discard("c")
A.discard("e")
B.discard('z')

print(A)
print(B)

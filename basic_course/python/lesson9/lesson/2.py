# def f(s):
#     ss = ''
#     for i in s:
#         ss+= i+'-'
#     return ss[:-1]

def printme(s):
    my_str = str(s)
    s2 = '-'.join(my_str)
    print('*** '+ s2 +' ***')

print('Hello')

test = 123
printme(test)

my_input = input('Сатр: ')
printme(my_input)

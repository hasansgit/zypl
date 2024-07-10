from random import randrange
a = randrange(1,100)
print('Компьютер ададеро байни 1 ва 100 "фикр" кард.')
print('Онро ёбед.')
n = int(input('Ададро дохил кунед:'))
while n != a:
    if n > a:
        print('Адади калонтарро дохил намудед.')
    else:
        print('Адади хурдтарро дохил намудед.')
    n = int(input('Ададро дохил кунед:'))
print('Шумо ададро ёфтед!')
print(f'a = {a}')

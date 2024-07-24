from datetime import date
from datetime import datetime
print(datetime.now())
print(datetime.now().date())
x = datetime.now()
print(x)
print(type(x))
y = x.date()
print(y)
print(type(y))

f_date = date(2024,6,21)
l_date = datetime.now().date()
delta = l_date - f_date
print(delta.days)
print(type(delta))
_year = int(input('Сол:'))
_month = int(input('Моҳ:'))
_day= int(input('Рӯз:'))

f_date = date(_year, _month, _day)
l_date = datetime.now().date()
delta = l_date - f_date
print(delta.days)

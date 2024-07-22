from datetime import datetime
x = datetime.now()
y = datetime(*map(int,input().split()))
print(f'{(x-y).days} days')

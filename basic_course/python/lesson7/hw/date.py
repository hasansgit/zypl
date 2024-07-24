from datetime import datetime
x = datetime.now()
y = datetime(*map(int,input().split()))
print((x-y).days)

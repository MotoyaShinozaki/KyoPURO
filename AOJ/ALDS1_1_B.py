x, y = map(int,input().split())
if x<y:
    a = x
    x = y
    y = a

while y>0:
    r = x%y
    x = y
    y = r
print(x)
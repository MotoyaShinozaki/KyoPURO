n = int(input())
r = [int(input().strip()) for _ in range(n)]
maxv = -1e9
minv = r[0]
for i in range(1,n):
    maxv = maxv if maxv > r[i]-minv else r[i]-minv
    minv = minv if minv < r[i] else r[i]
print(maxv)
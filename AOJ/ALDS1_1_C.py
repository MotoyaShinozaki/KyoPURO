def judge(n):
    if n == 2:
        return True
    elif n < 2 or n%2 == 0:
        return False
    else:
        i = 3
        while i<=n**0.5:
            if n%i==0:
                return False
            i = i + 2
    return True        

n = int(input())
num = [int(input().strip()) for _ in range(n)]

sum = 0
for i in range(n):
    if judge(num[i]):
        sum = sum + 1
print(sum)
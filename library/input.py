# 入力は以下の形式で標準入力から与えられる 
# N
n = int(input()) #文字列の場合はint()を外す

# 入力は以下の形式で標準入力から与えられる
# N M
n = int(input())
m = int(input())

# 入力は以下の形式で標準入力から与えられる
# A_0 A_1 A_2 ... A_N
a = list(map(int,input().split())) 

# 入力は以下の形式で標準入力から与えられる
# N
# A_1
# A_2
# ...
# A_N
n = int(input())
a = [int(input().strip()) for _ in range(n)]

# 入力は以下の形式で標準入力から与えられる
# N M
# A_11 A_12 A_13 ... A_1M
# A_21 A_22 A_23 ... A_2M
# ...                ...
# A_N1 A_N2 A_N2 ... A_NM
n, m = map(int,input().split())
a = [list(map(int,input().split())) for i in range(n)]

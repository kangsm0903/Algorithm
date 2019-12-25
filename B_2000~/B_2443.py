# 12/25 2443번

N = int(input())
M = 0
for i in range(2*N-1, -1, -2):
    a = ' '*(M)
    b = '*'*i
    M += 1
    print(a+b)
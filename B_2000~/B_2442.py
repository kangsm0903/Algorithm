# 12/24 2442번

N = int(input())
M = N
for i in range(1, 2*N+1, 2):
    a = ' '*(M-1)
    b = '*'*i
    M -= 1
    print(a+b)
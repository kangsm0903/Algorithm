# 12/26 2444번

N = int(input())
M = N

for i in range(1, 2*N+1, 2):
    a = ' '*(M-1)
    b = '*'*i
    M -= 1
    print(a+b)

M = 1
for i in range(2*N-3, -1, -2):
    a = ' '*(M)
    b = '*'*i
    M += 1
    print(a+b)
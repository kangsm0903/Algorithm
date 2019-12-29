N = int(input())

M = 0

for i in range(2*N-1, 2, -2):
    a = ' '*(M)
    b = '*'*i
    M += 1
    print(a+b)

M = N

for i in range(1, 2*N+1, 2):
    a = ' '*(M-1)
    b = '*'*i
    M -= 1
    print(a+b)

# -------------------------------------------------------------------------------------

# N = int(input())

# for i in range(N-1, 0, -1):
#     print(' '*(N-i-1)+('*'*(2*i+1)))

# for i in range(N):
#     print(' '*(N-i-1)+('*'*(2*i+1)))
# 12/28 2445번

N = int(input()) # 5

M = N*2-2

for i in range(1, N+1):
    a = '*'*i
    b = ' '*M

    M -= 2
    
    if M == -2:
        M += 2

    print(a+b+a)

for i in range(N-1, 0, -1):

    M += 2

    a = "*"*i
    b = ' '*M

    print(a+b+a)
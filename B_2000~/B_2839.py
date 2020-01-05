# 2020/01/05 2839번(설탕배달)

N = int(input())
M = []
for i in range(0,N):
    for k in range(0,N):
        if 5*k + 3*i == N:
            M.append(k+i)

try:
    print(min(M))
except ValueError:
    print(-1)
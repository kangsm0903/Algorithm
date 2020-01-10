# 2020/01/10 2751번 pypy3로 제출

N = int(input())

M = []

for i in range(0, N):
    M.append(int(input()))

for i in sorted(M):
    print(i)
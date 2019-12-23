# 12/23 2441번

N = int(input())

for i in range(N, -1, -1):
    a = '*'*i
    print(a.rjust(N))
# 12/17 2751번

N = int(input())

K = []

for i in range(0, N):
    M = int(input())
    K.append(M)

K = sorted(K, reverse=False)

for i in range(0, len(K)):
    print(K[i])
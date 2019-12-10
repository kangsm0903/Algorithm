# 12/11 2675번

N = int(input())

H = []

for i in range(0,N):
    K = list(input().split()) # [3,ABC]
    R = K[0] # 3
    S = list(K[1]) # [A, B, C]

    M = []

    for k in S:
        for l in range(0, int(R)):
            M.append(k)
    H.append(''.join(M))

for v in range(0, len(H)):
    print(H[v])
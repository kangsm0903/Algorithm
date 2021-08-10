#기타줄 
N, M = map(int, input().split())

A = []
B = [] # solo
C = [] # 6 set
D = [] # sole + 6set

for i in range(M):
    A.append(list(map(int, input().split())))

for i in range(M):
    B.append(A[i][1])
    C.append(A[i][0])
    D.append(A[i][0])
    D.append(A[i][1]*6)

if N < 6:
    if min(C) < min(B):
        print(min(C)*N)
    else:
        print(min(B)*N)
else:
    if (N%6)*min(B) >= min(C):
        print((N//6)*min(D) + min(C))
    elif (N%6)*min(B) < min(C):
        print((N//6)*min(D) + (N%6)*min(B))

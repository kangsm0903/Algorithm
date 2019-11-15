# # 11/15 10871번

N,X = input().split()

N = int(N)
X = int(X)

A = list(map(int,input().split()))
B = []
for i in range(0, N):
    if (A[i] < X) :
        print(A[i], end=' ')
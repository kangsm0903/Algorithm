# 2020/01/01 10953번

N = int(input())

B = []

for i in range(N):
    A = list(map(int, input().split(',')))
    B.append(A[0] + A[1])

for i in range(0, len(B)):
    print(B[i])
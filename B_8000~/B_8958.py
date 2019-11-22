# 11/22 8958번

N = int(input())

A = {}

for i in range(0,N):
    A[i] = input().split('X')

print(A)

B = []
C = []

for i in range(0,N):
    for k in range(0,len(A[i])):
        P = len(A[i][k])
        B.append(P*(P+1)/2)
    C.append(B)
        

print(B)
print(C)    
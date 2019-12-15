# 12/15 10870번

N = int(input())

A = [0, 1]

# A.append(A[0] + A[1])

for i in range(0,N-1):
    A.append(A[i]+A[i+1])

print(A[N])
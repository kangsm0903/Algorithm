N = list(map(int, input().split()))

A = 0

for i in range(0, len(N)):
    A += (N[i])**2

print(A%10)
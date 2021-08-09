N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = []

for i in range(N):
    result.append(max(B)*min(A))
    B.remove(max(B))
    A.remove(min(A))

print(sum(result))
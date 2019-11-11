#11/8
# 10817번

A = list(map(int, input().split())) #이거 된다. 오졌다.

A.remove(max(A))

if A[0]>A[1]:
    print(A[0])
else:
    print(A[1])
# .F.F...F
# F...F.F.

A = []

count = 0

for i in range(0,8):
    B = list(input())
    A.append(B)

for k in range(0,8):
    if k == 0 or k % 2 == 0:
        for l in range(0,8):
            if l % 2 == 0 and A[k][l] == 'F':
                count += 1
            elif l == 0 and A[k][l] == 'F':
                count += 1
    elif k % 2 != 0:
        for j in range(0,8):
            if j % 2 == 1 and A[k][j] == 'F':
                count += 1
print(count)
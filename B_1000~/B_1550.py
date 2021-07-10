N = list(input())
M = []

for i in range(0, len(N)):
    if N[i] == 'A':
        N[i] = 10
    elif N[i] == 'B':
        N[i] = 11
    elif N[i] == 'C':
        N[i] = 12
    elif N[i] == 'D':
        N[i] = 13
    elif N[i] == 'E':
        N[i] = 14
    elif N[i] == 'F':
        N[i] = 15
    else:
        N[i] = int(N[i])

for m in range(len(N)-1, -1, -1):
    M.append(16**m)

result = [x*y for x,y in zip(N,M)]

print(sum(result))
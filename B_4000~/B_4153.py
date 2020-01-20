# 2020/01/20 4153번

A = []

while True:
    N = list(map(int, input().split(' ')))
    if N[0] == 0 and N[1] == 0  and N[2] == 0:
        break
    else:
        Z = max(N)
        N.remove(max(N))
        if N[0]**2 + N[1]**2 == Z**2:
            A.append('right')
        else:
            A.append('wrong')

for i in A:
    print(i)
d = []
for i in range(0,19):
    d.append([])
    for j in range(0,19):
        d[i].append(0)

a = int(input())
for i in range(a):
    x,y=input().split(" ")
    x=int(x)
    y=int(y)
    d[x-1][y-1]=1

for l in range(0,19):
    for j in range(0,19):
        print(d[l][j],end=" ")
    print()


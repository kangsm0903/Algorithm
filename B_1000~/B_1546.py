# 11/19 1546번

N = int(input())

a = []
b = []

a.append(list(map(int, input().split())))

a.append(max(a[0]))

for i in range(0,N):
    b.append(a[0][i]/a[1])

c = sum(b)/N*100

print(c)
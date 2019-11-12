H = input()

H = int(H)

a = []
b = []

for i in range(1, H+1):
    a.append(list(map(int, input().split())))
    b.append(a[i-1])

for i in range(1, H+1):
    print("Case #{}: {}".format(i, sum(b[i-1])))
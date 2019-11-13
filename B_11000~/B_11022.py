# 11/13 11022번

T = input()
T = int(T)

a = []
b = []

for i in range(1,T+1):
    a.append(list(map(int, input().split())))
    b.append(sum(a[i-1]))
    
for i in range(1, T+1):
    print("Case #{}: {} + {} = {}".format(i, a[i-1][0], a[i-1][1], b[i-1]))
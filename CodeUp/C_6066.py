a = list(map(int, input().split(" ")))

for i in range(0,3):
    if a[i]%2 == 0:
        a[i] = "even"
    else:
        a[i] = "odd"

for i in range(0,3):
    print(a[i])
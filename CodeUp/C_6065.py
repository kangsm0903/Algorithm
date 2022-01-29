a = list(map(int,input().split(" ")))
b = []
for i in range(0,3):
    if a[i]%2 == 0:
        b.append(a[i])
    
for i in range(0,len(b)):
    print(b[i])
# 11/20 2577번

A = int(input())
B = int(input())
C = int(input())

D = A*B*C

k = 0

a = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

while D > 10**k:
    k += 1
    

E = []

for i in range(k-1,-1, -1):
    E.append(D//(10**i))
    D = D - (10**i)*(D//(10**i))

for i in range(0, len(E)):
    for m in range(0,10):
        if E[i] == m:
            a[m] += 1
       
for i in range(0,10):
    print(a[i])
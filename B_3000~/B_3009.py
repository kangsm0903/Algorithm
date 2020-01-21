# 2020/01/21 3009번

N = []

for i in range(3):
    N.append(list(map(int, input().split())))

X = []
X.append(N[0][0])
X.append(N[1][0])
X.append(N[2][0])

Y = []
Y.append(N[0][1])
Y.append(N[1][1])
Y.append(N[2][1])

for i in X:
    if X.count(i) == 2:
        X.remove(i)
        X.remove(i)
    else:
        pass
for k in Y:
    if Y.count(k) == 2:
        Y.remove(k)
        Y.remove(k)
    else:
        pass

X.append(Y[0])

Z = []
for m in X:
    Z.append(str(m))

print(' '.join(Z))
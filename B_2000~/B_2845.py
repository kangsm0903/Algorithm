N = list(map(int, input().split()))
M = N[0]*N[1]

K = 'first'

L = list(map(int, input().split()))

for i in L:
    K = K + ' ' + str(i-M)

K = K.replace('first ','')

print(K)
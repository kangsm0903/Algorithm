# 12/20 

N = list(map(int, input().split()))

N.append(N[1]-N[0])
N.remove(N[0])
N.reverse()
N = [str(i) for i in N]

A = ' '.join(N)

print(A)
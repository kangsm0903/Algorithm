# 12/12 1157번 
# upper() / lower() 대문자 소문자 
# operator.itemgetter - dictionary를 정렬할 때 주로 쓴다. 0 - keys / 1 - values
import operator

N = input().lower()

N = list(N) # [M,i,s,s,i,s,s,i,p,i]
M = list(set(N)) # [M,i,s,p]
A = {}
for i in M:
    A[i] = N.count(i) # {M:1, s:4, i:4, p:1}

L = 0

for k in A:
    if A.get(k) == max(A.values()):
        L += 1
    else:
        pass
if L > 1:
    print('?')
else:
    print(max(A.items(), key=operator.itemgetter(1))[0].upper())
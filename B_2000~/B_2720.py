import sys

S=int(sys.stdin.readline())

case=[25,10,5,1]

total=[]

for i in range(S):
    A=int(sys.stdin.readline())
    sub=[]
    for k in case:
        sub.append(A//k)
        A=A%k
    total.append(sub)

for i in total:
    for k in i:
        print(k,end=' ')
    print()
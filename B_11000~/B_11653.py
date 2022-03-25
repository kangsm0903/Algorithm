import sys

N=int(sys.stdin.readline())

total=[]
base=2

while N!=1:
    if N%base==0:
        N=N//base
        total.append(base)
    else:
        base+=1

for i in total:
    print(i)
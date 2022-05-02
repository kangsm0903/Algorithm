import sys

N=int(sys.stdin.readline())

case=[]

for i in range(N):
    element=int(sys.stdin.readline())
    if element==0:
        case.pop()
    else:
        case.append(element)

print(sum(case))
import sys

N=int(sys.stdin.readline())

case=list(map(int,sys.stdin.readline().split()))

result=[]

for i in range(0,len(case)):
    cnt=0
    for k in range(i+1,len(case)):
        if case[i]<case[k]:
            break
        else:
            cnt+=1
    result.append(cnt)

print(max(result))
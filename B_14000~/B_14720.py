N=int(input())

case=list(map(int,input().split()))

now=0
count=0

for i in range(N):
    if now==3:
        now=0

    if case[i]==now:
        now+=1
        count+=1
    else:
        pass

print(count)
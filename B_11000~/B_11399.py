a=int(input())
b=list(map(int,input().split()))
b.sort()
total=0
all=0
for i in range(a):
    total=total+b[i]
    all=all+total
print(all)
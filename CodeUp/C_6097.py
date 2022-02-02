a,b=input().split(" ")
A=[]
for i in range(int(a)):
    A.append([])
    for k in range(int(b)):
        A[i].append(0)

c=int(input())
for i in range(c):
    d=list(map(int,input().split( )))
    A[d[2]-1][d[3]-1]=1
    count=0
    for l in range(d[0]):
        if d[1]==0:
            A[d[2]-1][d[3]+count-1]=1
            count+=1
        else:
            A[d[2]+count-1][d[3]-1]=1
            count+=1

for m in range(int(a)):
    for n in range(int(b)):
        print(A[m][n],end=' ')
    print( )
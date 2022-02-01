a=[]
for i in range(19): # 5*5
    a.append(list(map(int,input().split( ))))
b=int(input())
for l in range(b):
    x,y=input().split(" ")
    x = int(x)-1
    y = int(y)-1
    for k in range(19):
        if a[x][k]==1:
            a[x][k]=0
        else:
            a[x][k]=1

        if a[k][y]==1:
            a[k][y]=0
        else:
            a[k][y]=1

for i in range(19):
    for j in range(19):
        print(a[i][j],end=' ')
    print()
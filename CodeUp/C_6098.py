a=[]

for i in range(10):
    b = list(map(int, input().split(" ")))
    a.append(b)

X = [1,1]

while a[X[0]][X[1]]!=2:
    a[X[0]][X[1]]=9
    if a[X[0]][X[1]+1]==0 or a[X[0]][X[1]+1]==2:
        X[1]+=1
    elif a[X[0]+1][X[1]]==1:
        break
    elif a[X[0]][X[1]+1]==1:
        X[0]+=1
    else:
        break

a[X[0]][X[1]]=9

for i in range(10):
    for k in range(10):
        print(a[i][k], end=' ')
    print( )
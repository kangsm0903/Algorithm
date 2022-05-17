A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

total=[]

total.append(A.count(0))
total.append(B.count(0))
total.append(C.count(0))

for i in total:
    if i==1:
        print('A')
    elif i==2:
        print('B')
    elif i==3:
        print('C')
    elif i==4:
        print('D')
    elif i==0:
        print('E')
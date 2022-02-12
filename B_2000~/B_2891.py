# 카약을 나누어줄때 탐색을 오른쪽부터하면 틀리고 왼쪽부터하면 맞음
# 이 부분을 조금 더 알아봐야할 듯 (25, 27번줄을 서로 바꾸면 틀림 - Why?)

N,S,R=input().split() # N=team S=damage R=remain
X=[]
for i in range(1,int(N)+1): # X=[1,2,3,4,5,6,7,8,9,10]
    X.append(i)

Sn=list(map(int,input().split())) # Sn=[1,2,3,4,5]

for i in Sn: # X=[6,7,8,9,10]
    X.remove(i)

Rn=list(map(int,input().split())) # Rn=[1,2,3,8,9]

for i in Sn: 
    if i in Rn:
        X.append(i)
        Rn.remove(i)
    else:
        pass

for i in Rn:
    X.sort()
    if i-1 not in X and i-1>0:
        X.append(i-1)
    elif i+1 not in X and i+1<=int(N):
        X.append(i+1)
    else:
        pass
print(int(N)-len(X))
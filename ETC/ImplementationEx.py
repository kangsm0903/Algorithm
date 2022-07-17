N=int(input()) # 1<=N<=100

case=list(map(str,input().split()))
# 1<=이동횟수<=100

start=[1,1]

for i in case:
    if i=='L' and start[1]-1>=1:
        start[1]-=1

    elif i=='R' and start[1]+1<=N:
        start[1]+=1

    elif i=='U' and start[0]-1>=1:
        start[0]-=1

    elif i=='D' and start[0]+1<=N:
        start[0]+=1

print(start)

# ------------------------------------------------------
# 이동 벡터 nx=x+dx / ny=y+dy 

n=int(input())
x,y=1,1
plans=input().split() # R R R U D D

dx=[0,0,-1,1] # U / D
dy=[-1,1,0,0] # L / R
move_types=['L','R','U','D']

for plan in plans: # 하나씩 들어옴
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]

    # 공간을 벗어난 경우 continue
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    
    # 이동 수행
    x,y=nx,ny
print(x,y)
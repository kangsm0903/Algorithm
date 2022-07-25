# 기존 토마토 2차원 배열 문제를 3차원 배열을 추가하여 푸는 문제
# x,y,z의 범위를 제한할 때 헷갈리는 부분이 있었으며 (35번)
# 3차원 배열을 만들어주는 부분도 처음에는 생소하여 헤맸던 것이 아쉬웠음

# 토마토에 z축 추가

from collections import deque

X,Y,Z=map(int,input().split())

graph=[]
queue=deque()

for i in range(Z): # 2
    tmp=[]
    for j in range(Y): # 3
        tmp.append(list(map(int,input().split())))
    graph.append(tmp)

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]

for i in range(Z):
    for j in range(Y):
        for k in range(X):
            if graph[i][j][k]==1:
                queue.append((i,j,k))

def bfs():
    while queue:
        z,y,x=queue.popleft()

        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]

            if 0<=nx<X and 0<=ny<Y and 0<=nz<Z:
                if graph[nz][ny][nx]==0:
                    graph[nz][ny][nx]=graph[z][y][x]+1
                    queue.append((nz,ny,nx))

bfs()

breaker=False
result=0

for i in graph:
    for j in i:
        if 0 in j:
            result=0
            breaker=True
            break
        result=max(result,max(j))
    if breaker==True:
        break

print(result-1)